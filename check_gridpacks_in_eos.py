import os,sys

# ##############################################
# ############ CHECK EOS PERMISSIONS ###########
# ##############################################
# print('assign 755 to all EOS gridpack directories'); sys.stdout.flush()
# os.system('find /eos/cms/store/group/phys_generator/cvmfs/gridpacks/ -type d -exec chmod 755 {} +')
# print('assign 644 to all EOS gridpack files'); sys.stdout.flush()
# os.system('find /eos/cms/store/group/phys_generator/cvmfs/gridpacks/ -type f -exec chmod 644 {} +');
# sys.exit(1)
# ##############################################
# ########## END CHECK EOS PERMISSIONS #########
# ##############################################

my_path = '/tmp/'+os.environ['USER']+'/replace_gridpacks/'

requests = [
'B2G-RunIISummer15wmLHEGS-01362',
'B2G-RunIISummer15wmLHEGS-01363',
'B2G-RunIISummer15wmLHEGS-01364',
'B2G-RunIISummer15wmLHEGS-01365',
'B2G-RunIISummer15wmLHEGS-01366',
'B2G-RunIISummer15wmLHEGS-01367',
'B2G-RunIISummer15wmLHEGS-01368',
'B2G-RunIISummer15wmLHEGS-01369',
'B2G-RunIISummer15wmLHEGS-01370',
'B2G-RunIISummer15wmLHEGS-01371',
'B2G-RunIISummer15wmLHEGS-01372',
'B2G-RunIISummer15wmLHEGS-01373',
'B2G-RunIISummer15wmLHEGS-01374',
'B2G-RunIISummer15wmLHEGS-01375',
'B2G-RunIISummer15wmLHEGS-01376',
'B2G-RunIISummer15wmLHEGS-01377',
'B2G-RunIISummer15wmLHEGS-01378',
'B2G-RunIISummer15wmLHEGS-01379',
'B2G-RunIISummer15wmLHEGS-01380',
'B2G-RunIISummer15wmLHEGS-01381',
'B2G-RunIISummer15wmLHEGS-01382',
'B2G-RunIISummer15wmLHEGS-01383',
'B2G-RunIISummer15wmLHEGS-01384',
'B2G-RunIISummer15wmLHEGS-01385',
'B2G-RunIISummer15wmLHEGS-01386',
'B2G-RunIISummer15wmLHEGS-01387',
'B2G-RunIISummer15wmLHEGS-01526',
'B2G-RunIISummer15wmLHEGS-01527',
'B2G-RunIISummer15wmLHEGS-01528',
'B2G-RunIISummer15wmLHEGS-01529',
'B2G-RunIISummer15wmLHEGS-01530',
'B2G-RunIISummer15wmLHEGS-01531',
'B2G-RunIISummer15wmLHEGS-01532',
'B2G-RunIISummer15wmLHEGS-01533',
'B2G-RunIISummer15wmLHEGS-01534',
'B2G-RunIISummer15wmLHEGS-01535',
'B2G-RunIISummer15wmLHEGS-01536',
'B2G-RunIISummer15wmLHEGS-01537',
'B2G-RunIISummer15wmLHEGS-01538',
'B2G-RunIISummer15wmLHEGS-01539',
'B2G-RunIISummer15wmLHEGS-01540',
'B2G-RunIISummer15wmLHEGS-01541',
'B2G-RunIISummer15wmLHEGS-01542',
'B2G-RunIISummer15wmLHEGS-01543',
'B2G-RunIISummer15wmLHEGS-01544',
'B2G-RunIISummer15wmLHEGS-01545',
'B2G-RunIISummer15wmLHEGS-01546',
'B2G-RunIISummer15wmLHEGS-01548',
'B2G-RunIISummer15wmLHEGS-01550',
'B2G-RunIISummer15wmLHEGS-01551',
'B2G-RunIISummer15wmLHEGS-01553',
'B2G-RunIISummer15wmLHEGS-01554',
'B2G-RunIISummer15wmLHEGS-01556',
'B2G-RunIISummer15wmLHEGS-01557',
'B2G-RunIISummer15wmLHEGS-01559',
'B2G-RunIISummer15wmLHEGS-01561',
'B2G-RunIISummer15wmLHEGS-01563',
'B2G-RunIISummer15wmLHEGS-01565',
'B2G-RunIISummer15wmLHEGS-01567',
'B2G-RunIISummer15wmLHEGS-01568',
'B2G-RunIISummer15wmLHEGS-01569',
'B2G-RunIISummer15wmLHEGS-01570',
'B2G-RunIISummer15wmLHEGS-01571',
'B2G-RunIISummer15wmLHEGS-01572',
'B2G-RunIISummer15wmLHEGS-01573',
'B2G-RunIISummer15wmLHEGS-01574',
'B2G-RunIISummer15wmLHEGS-01575',
'B2G-RunIISummer15wmLHEGS-01576',
'B2G-RunIISummer15wmLHEGS-01577',
'B2G-RunIISummer15wmLHEGS-01578',
'B2G-RunIISummer15wmLHEGS-01579',
'B2G-RunIISummer15wmLHEGS-01580',
'B2G-RunIISummer15wmLHEGS-01581',
'B2G-RunIISummer15wmLHEGS-01582',
'EXO-RunIISummer15wmLHEGS-04800',
'EXO-RunIISummer15wmLHEGS-04801',
'EXO-RunIISummer15wmLHEGS-04803',
'EXO-RunIISummer15wmLHEGS-04960',
'EXO-RunIISummer15wmLHEGS-04975',
'EXO-RunIISummer15wmLHEGS-05186',
'EXO-RunIISummer15wmLHEGS-05187',
'EXO-RunIISummer15wmLHEGS-05190',
'EXO-RunIISummer15wmLHEGS-05193',
'EXO-RunIISummer15wmLHEGS-05198',
'EXO-RunIISummer15wmLHEGS-05204',
'EXO-RunIISummer15wmLHEGS-05205',
'EXO-RunIISummer15wmLHEGS-05208',
'EXO-RunIISummer15wmLHEGS-05209',
'EXO-RunIISummer15wmLHEGS-05210',
'EXO-RunIISummer15wmLHEGS-05212',
'EXO-RunIISummer15wmLHEGS-05213',
'EXO-RunIISummer15wmLHEGS-05215',
'EXO-RunIISummer15wmLHEGS-05216',
'EXO-RunIISummer15wmLHEGS-05217',
'FSQ-RunIISummer15wmLHEGS-00003',
'FSQ-RunIISummer15wmLHEGS-00005',
'FSQ-RunIISummer15wmLHEGS-00006',
'FSQ-RunIISummer15wmLHEGS-00007',
'FSQ-RunIISummer15wmLHEGS-00008',
'FSQ-RunIISummer15wmLHEGS-00009',
'FSQ-RunIISummer15wmLHEGS-00011',
'FSQ-RunIISummer15wmLHEGS-00012',
'FSQ-RunIISummer15wmLHEGS-00014',
'HIG-RunIISummer15wmLHEGS-01579',
'HIG-RunIISummer15wmLHEGS-01580',
'HIG-RunIISummer15wmLHEGS-01581',
'HIG-RunIISummer15wmLHEGS-01582',
'HIG-RunIISummer15wmLHEGS-01583',
'HIG-RunIISummer15wmLHEGS-01585',
'HIG-RunIISummer15wmLHEGS-01586',
'HIG-RunIISummer15wmLHEGS-01587',
'HIG-RunIISummer15wmLHEGS-01588',
'HIG-RunIISummer15wmLHEGS-01589',
'HIG-RunIISummer15wmLHEGS-01593',
'HIG-RunIISummer15wmLHEGS-01595',
'HIG-RunIISummer15wmLHEGS-01596',
'HIG-RunIISummer15wmLHEGS-01597',
'HIG-RunIISummer15wmLHEGS-01600',
'HIG-RunIISummer15wmLHEGS-01601',
'HIG-RunIISummer15wmLHEGS-01602',
'HIG-RunIISummer15wmLHEGS-01605',
'HIG-RunIISummer15wmLHEGS-01606',
'HIG-RunIISummer15wmLHEGS-01607',
'HIG-RunIISummer15wmLHEGS-01614',
'HIG-RunIISummer15wmLHEGS-01616',
'HIG-RunIISummer15wmLHEGS-01617',
'HIG-RunIISummer15wmLHEGS-01618',
'HIG-RunIISummer15wmLHEGS-01620',
'HIG-RunIISummer15wmLHEGS-01622',
'HIG-RunIISummer15wmLHEGS-01623',
'HIG-RunIISummer15wmLHEGS-01625',
'HIG-RunIISummer15wmLHEGS-01626',
'HIG-RunIISummer15wmLHEGS-01627',
'HIG-RunIISummer15wmLHEGS-01630',
'HIG-RunIISummer15wmLHEGS-01631',
'HIG-RunIISummer15wmLHEGS-01632',
'HIG-RunIISummer15wmLHEGS-01634',
'HIG-RunIISummer15wmLHEGS-01635',
'HIG-RunIISummer15wmLHEGS-01636',
'HIG-RunIISummer15wmLHEGS-01639',
'HIG-RunIISummer15wmLHEGS-01642',
'HIG-RunIISummer15wmLHEGS-01643',
'HIG-RunIISummer15wmLHEGS-01660',
'HIG-RunIISummer15wmLHEGS-01662',
'HIG-RunIISummer15wmLHEGS-01663',
'HIG-RunIISummer15wmLHEGS-01664',
'HIG-RunIISummer15wmLHEGS-01665',
'HIG-RunIISummer15wmLHEGS-01668',
'HIG-RunIISummer15wmLHEGS-01669',
'HIG-RunIISummer15wmLHEGS-01670',
'HIG-RunIISummer15wmLHEGS-01672',
'HIG-RunIISummer15wmLHEGS-01673',
'HIG-RunIISummer15wmLHEGS-01674',
'HIG-RunIISummer15wmLHEGS-01675',
'HIG-RunIISummer15wmLHEGS-01676',
'HIG-RunIISummer15wmLHEGS-01677',
'HIG-RunIISummer15wmLHEGS-01680',
'HIG-RunIISummer15wmLHEGS-01681',
'HIG-RunIISummer15wmLHEGS-01683',
'HIG-RunIISummer15wmLHEGS-01684',
'HIG-RunIISummer15wmLHEGS-01687',
'HIG-RunIISummer15wmLHEGS-01688',
'HIG-RunIISummer15wmLHEGS-01689',
'HIG-RunIISummer15wmLHEGS-01690',
'HIG-RunIISummer15wmLHEGS-01691',
'HIG-RunIISummer15wmLHEGS-01692',
'HIG-RunIISummer15wmLHEGS-01693',
'HIG-RunIISummer15wmLHEGS-01694',
'HIG-RunIISummer15wmLHEGS-01695',
'HIG-RunIISummer15wmLHEGS-01739',
'HIG-RunIISummer15wmLHEGS-01740',
'SMP-RunIISummer15wmLHEGS-00119',
'SMP-RunIISummer15wmLHEGS-00174',
'SMP-RunIISummer15wmLHEGS-00201',
'SMP-RunIISummer15wmLHEGS-00202',
'SMP-RunIISummer15wmLHEGS-00203',
'SMP-RunIISummer15wmLHEGS-00204',
'SMP-RunIISummer15wmLHEGS-00205',
'SMP-RunIISummer15wmLHEGS-00206',
'SMP-RunIISummer15wmLHEGS-00207',
'SMP-RunIISummer15wmLHEGS-00208',
'SMP-RunIISummer15wmLHEGS-00209',
'SMP-RunIISummer15wmLHEGS-00210',
'SMP-RunIISummer15wmLHEGS-00211',
'SMP-RunIISummer15wmLHEGS-00212',
'SMP-RunIISummer15wmLHEGS-00213',
'SMP-RunIISummer15wmLHEGS-00214',
'SMP-RunIISummer15wmLHEGS-00215',
'SMP-RunIISummer15wmLHEGS-00216',
'SMP-RunIISummer15wmLHEGS-00217',
'SMP-RunIISummer15wmLHEGS-00218',
'SMP-RunIISummer15wmLHEGS-00219',
'SMP-RunIISummer15wmLHEGS-00220',
'SUS-RunIISummer15wmLHEGS-00187',
           ]

path1 = '/cvmfs/cms.cern.ch/phys_generator'
path2 = '/eos/cms/store/group/phys_generator/cvmf'
print(path1)
print(path2)
##########################################
######## START LOOP OVER PREPIDS #########
##########################################
for prepid in requests:

        os.system('echo '+prepid)
        
        os.system('mkdir -p '+my_path+'/'+prepid)
        os.chdir(my_path+'/'+prepid)
        os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+prepid+' -O '+prepid)
        gridpack_cvmfs_path = os.popen('grep \/cvmfs '+prepid).read()
        gridpack_cvmfs_path = gridpack_cvmfs_path.split('\'')[1]
#	print type(gridpack_cvmfs_path)
#	print (gridpack_cvmfs_path)
	gridpack_eos_path = gridpack_cvmfs_path.replace("/cvmfs/cms.cern.ch/phys_generator","/eos/cms/store/group/phys_generator/cvmfs")
#	print (gridpack_eos_path)	
	os.system('tar xf '+gridpack_eos_path+' -C'+my_path+'/'+prepid)
	os.system('more '+my_path+'/'+prepid+'/'+'runcmsgrid.sh | grep "FORCE IT TO"')
	os.system('grep _CONDOR_SCRATCH_DIR '+my_path+'/'+prepid+'/'+'mgbasedir/Template/LO/SubProcesses/refine.sh')
        os.system('grep "= ickkw" '+my_path+'/'+prepid+'/'+'process/madevent/Cards/run_card.dat')
	os.system('echo "------------------------------------"')
	os.system('rm '+prepid)
##########################################
######## END LOOP OVER PREPIDS ###########
##########################################



#        gridpack_eos_path = gridpack_cvmfs_path.replace('/cvmfs/cms.cern.ch/phys_generator/gridpacks/','/eos/cms/store/group/phys_generator/cvmfs/gridpacks/')
           
