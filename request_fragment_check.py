import os,sys,time,string,re
os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps
from itertools import groupby

mcm = McM(dev=False)

query_str = 'prepid='+str(sys.argv[1])
res = mcm.get('requests', query=query_str)
if len(res) == 0 :
    print "***********************************************************************************"
    print "Something's wrong - can not get the request parameters"
    print "***********************************************************************************"
    exit()

my_path =  '/tmp/'+os.environ['USER']+'/gridpacks/'
print ""
print "***********************************************************************************"

for r in res:
    pi = r['prepid']
    dn = r['dataset_name']
    te = r['time_event']
    totalevents = r['total_events']
    cmssw = r['cmssw_release']
    print (pi)
    check = []
    tunecheck = []
    psweightscheck = []
    ME = ["PowhegEmissionVeto","aMCatNLO"]
    MEname = ["powheg","madgraph","mcatnlo"]
    tunename = ["CP5","CUETP8M1"]
    tune = ["CP5","CUEP8M1"] 
    matching = 10
    ickkw = 'del'
    for item in te:
        timeperevent = float(item)
    if timeperevent > 150.0 :
        print "* [WARNING] Large time/event - please check"
    if '10_2' not in cmssw and '9_3' not in cmssw and '7_1' not in cmssw :
        print "* [WARNING] Are you sure you want to use "+cmssw+"release which is not standard"
        print "*           which may not have all the necessary GEN code."
    if totalevents >= 100000000 :
        print "* [WARNING] Is "+str(totalevents)+" events what you really wanted - please check!"
    fsize = os.popen('wget --spider --server-response https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O - 2>&1 | sed -ne \'/Length/{s/.*: //;p}\'').read()
    if 'unspecified' in fsize :
        os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/'+pi+' -O '+pi)
        gettest = os.popen('grep cff '+pi+' | grep curl').read()
        for index, aword in enumerate(MEname):
            if aword in dn.lower() :
                print "* "+gettest
                print "* [OK] Probably OK if the above hadronizer is what you intended to use"
            else:
                print "* [ERROR] Something may be wrong - name/hadronizer mismatch - please check!"
        print "***********************************************************************************"
        print ""
        exit()
    os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O '+pi)
    os.system('mkdir -p '+my_path+'/'+pi)
    if int(os.popen('grep -c eos '+pi).read()) == 1 :
        print "* [ERROR] Gridpack should have used cvmfs path instead of eos path"
    for ind, word in enumerate(MEname):
        if word in dn.lower() :
            if ind == 2 :
                knd = 1 
            else :
                knd = ind
            check.append(int(os.popen('grep -c pythia8'+ME[knd]+'Settings '+pi).read()))
            check.append(int(os.popen('grep -c "from Configuration.Generator.Pythia8'+ME[knd]+'Settings_cfi import *" '+pi).read()))
            check.append(int(os.popen('grep -c "pythia8'+ME[knd]+'SettingsBlock," '+pi).read()))
            if ind > 0 :
                 os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O '+my_path+'/'+pi+'/'+pi)
                 gridpack_cvmfs_path = os.popen('grep \/cvmfs '+my_path+'/'+pi+'/'+pi+'| grep -v \'#args\' ').read()
                 gridpack_cvmfs_path = gridpack_cvmfs_path.split('\'')[1]
                 os.system('tar xf '+gridpack_cvmfs_path+' -C'+my_path+'/'+pi)
                 fname = my_path+'/'+pi+'/'+'process/madevent/Cards/run_card.dat'
                 fname2 = my_path+'/'+pi+'/'+'process/Cards/run_card.dat'
                 if os.path.isfile(fname) is True :
                     ickkw = os.popen('grep "= ickkw" '+fname).read()
                 elif os.path.isfile(fname2) is True :    
                     ickkw = os.popen('grep "= ickkw" '+fname2).read()
                 ickkw = str(ickkw)    
                 matching = int(re.search(r'\d+',ickkw).group())
#            print (matching,check[0],check[1],check[2])     
            if matching >= 2 and check[0] == 2 and check[1] == 1 and check[2] == 1 :
                print "* [OK] no known inconsistency in the fragment w.r.t. the name of the dataset "+word
                if matching ==3 :  
                   print "* [WARNING] This is a FxFx sample. Please check 'JetMatching:nJetMax' is set correctly"
                   print "*                as number of partons in born matrix element for highest multiplicity."
                if matching > 3 :
                   print "* [WARNING] This is a Powheg NLO sample. Please check 'nFinal' is set correctly"
                   print "*                        as number of final state particles (BEFORE THE DECAYS)"
                   print "*                                   in the LHE other than emitted extra parton."
            elif matching == 1 and check[0] == 0 and check[1] == 0 and check[2] == 0 :    
                print "* [OK] no known inconsistency in the fragment w.r.t. the name of the dataset "+word
                print "* [WARNING] This is a MadGraph LO sample with Jet matching sample. Please check"
                print "*                   'JetMatching:nJetMax' is set correctly as number of partons"
                print "*                              in born matrix element for highest multiplicity."
	    elif matching == 0 and word == "madgraph" and check[0] == 0 and check[1] == 0 and check[2] == 0 :
		print "* [OK] no known inconsistency in the fragment w.r.t. the name of the dataset "+word
	    elif matching == 0 and word == "mcatnlo" and check[0] == 2 and check[1] == 1 and check[2] == 1 :
		print "* [OK] no known inconsistency in the fragment w.r.t. the name of the dataset "+word
                print "* [WARNING] This is a MadGraph NLO sample without matching. Please check 'TimeShower:nPartonsInBorn'"
                print "*                                                   is set correctly as number of coloured particles"
                print "*                                                  (before resonance decays) in born matrix element."
            else:     
                print "* [ERROR] May be wrong fragment: "+word+" in dataset name but settings in fragment not correct or vice versa"
                if word == "powheg" :
                   print "* [WARNING] if this is a"+word+" sample but a loop induced process such as ggZH," 
                   print "*           then fragment is OK (no need to have Pythia8PowhegEmissionVetoSettings)"
    for kk in range (0, 2):   
        tunecheck.append(int(os.popen('grep -c -i '+tune[kk]+' '+pi).read()))
    if tunecheck[0] < 3 and tunecheck[1] < 3 :
        print "* [ERROR] Tune configuration wrong in the fragment"
    elif tunecheck[0] > 2 or tunecheck[1] >2 :
        print "* [OK] Tune configuration probably OK in the fragment"
        if tunecheck[0] > 2 :
            if 'Fall18' not in pi and 'Fall17' not in pi :
                print "* [WARNING] Do you really want to have tune "+tunename[0] +" in this campaign?"
    if 'Fall18' in pi :
        if int(os.popen('grep -c "from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *" '+pi).read()) != 1 :
            print "* [WARNING] No parton shower weights configuration in the fragment. In the Fall18 campaign, we recommend to include Parton Shower weights"
        if int(os.popen('grep -c "from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *" '+pi).read()) == 1 :
	    if '10_2_3' not in cmssw :
		"* [ERROR] PS weights in config but CMSSW version is not 10_2_3 - please check!"
		exit() 		    
            psweightscheck.append(int(os.popen('grep -c "from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *" '+pi).read()))
            psweightscheck.append(int(os.popen('grep -c "pythia8PSweightsSettingsBlock," '+pi).read()))
            psweightscheck.append(int(os.popen('grep -c "pythia8PSweightsSettings" '+pi).read()))
            if psweightscheck[0] == 1 and psweightscheck[1] == 1 and psweightscheck[2] == 2 :
                print "* [OK] Parton shower weight configuration probably OK in the fragment"
            else:
                print "* [ERROR] Parton shower weight configuretion not OK in the fragment" 

    print "***********************************************************************************"
    print ""
