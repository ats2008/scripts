#!/usr/bin/python3

import os,sys,time
import string
import re
import argparse
import textwrap
from operator import itemgetter

#os.system('env -i KRB5CCNAME="$KRB5CCNAME" cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o cookiefile.txt --krb --reprocess')
#os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
#os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
#sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

#from rest import McM
from json import dumps,load
import numpy as np
from itertools import groupby
from textwrap import dedent
#import pandas as pd
#mcm = McM(cookie='cookiefile.txt', dev=False, debug=False)
#mcm = McM(id='no-id', dev=False, debug=False)
#mcm_link = "https://cms-pdmv.cern.ch/mcm/"

#def get_request(prepid):
#    result = mcm._McM__get('public/restapi/requests/get/%s' % (prepid))
#    if not result:
#        return {}
#
#    result = result.get('results', {})
#    return result



#dataMode="rest"

import sys

doAllPogs=True
FULL_DETAILS =False

if( len(sys.argv) >1):
   if "true"==sys.argv[1].lower():
   	FULL_DETAILS=True
if( len(sys.argv) >2):
   if "false"==sys.argv[2].lower():
   	doAllPogs=False
POG="SMP"
if( len(sys.argv) >3):
   POG=sys.argv[3]

dataMode="json"
HSO6_CONVERSION_FACTOR = 21.0
tot_kevt = 0
tot_cpu_ksec = 0
f = open("Revised20Jan2021genstudyDavid.txt",'r')

Lines = f.readlines()
itemCount=0

data={}
if dataMode=="json":
    with open('mcmResponse.json', 'r') as fp:
            data = load(fp)

exception_prepids =["SUS-RunIISummer20UL18wmLHEGEN-00044","EXO-RunIISummer20UL18wmLHEGEN-00130","SUS-RunIISummer20UL18GEN-00013","SUS-RunIISummer20UL18wmLHEGEN-00018","EXO-RunIISummer20UL18GEN-00075"]

compiledTags = {
'all' : 'ALL',
'lo': 'ALL LO',
'madgraph':'MG5_aMC',
'madgraphmlm':'madgraphMLM',
'pythia':'pythia8',
'pythiamlm':'pythiaMLM',
'nlo' : 'ALL NLO',
'>lo' : '>LO',
'herwig' : 'Herwig',
'powheg' : 'Powheg',
'amcatnlo':'amc@nlo',
'mlm' : 'mlm',
'openloops' : 'Powheg Openloops',
'fxfx' : 'FxFx',
'comphep' : 'comphep',
'photos' : 'PHOTOS',
'minnlo' : 'minnlo',
'nnlo' : 'All NNLO', 
'pythiaOnly' :'pythia8 Only',
'jhugen'     :'JHU Generator',
'evtgen'     :'EvtGen',
'madspin'    :'MadSpin',
}

#   ----------------------------------------------------- #

# ADD NEW TAG HERE and then add the corresponging update cmd in parsing the loop
compiledDataPOG={}
tires=['lo','nlo','nnlo','>lo']

compiledDataPOG['SMP']={'lo':{},'nlo':{}}
compiledDataPOG['SMP']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['SMP']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['HIG']={'lo':{},'nlo':{}}
compiledDataPOG['HIG']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['HIG']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['BPH']={'lo':{},'nlo':{}}
compiledDataPOG['BPH']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['BPH']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['TAU']={'lo':{},'nlo':{}}
compiledDataPOG['TAU']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['TAU']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['TOP']={'lo':{},'nlo':{}}
compiledDataPOG['TOP']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['TOP']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['SUS']={'lo':{},'nlo':{}}
compiledDataPOG['SUS']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['SUS']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['B2G']={'lo':{},'nlo':{}}
compiledDataPOG['B2G']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['B2G']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['EGM']={'lo':{},'nlo':{}}
compiledDataPOG['EGM']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['EGM']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['JME']={'lo':{},'nlo':{}}
compiledDataPOG['JME']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['JME']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['BTV']={'lo':{},'nlo':{}}
compiledDataPOG['BTV']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['BTV']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['PPD']={'lo':{},'nlo':{}}
compiledDataPOG['PPD']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['PPD']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}

compiledDataPOG['EXO']={'lo':{},'nlo':{}}
compiledDataPOG['EXO']['lo']={'madgraph':{},'pythia':{},'mlm':{},'comphep':{}}
compiledDataPOG['EXO']['nlo']={'minnlo':{},'fxfx':{},'openloops':{},'powheg':{},'amcatnlo':{}}


#   ----------------------------------------------------- #

# updating the compiledDataPOG with nthe data colums

headList=list(compiledDataPOG.keys())
for head in headList:
    compiledDataPOG[head][head+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
    kysList=list(compiledDataPOG[head].keys())
    for kys in kysList:
        if kys not in tires:
            continue
        compiledDataPOG[head][kys+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
        for kkys in compiledDataPOG[head][kys]:
            compiledDataPOG[head][kys][kkys]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
 
compiledData={}
tires=['lo','nlo','nnlo','>lo']

compiledData['v+jets']={'lo':{},'>lo':{}}
compiledData['v+jets']['lo']={'madgraph':{},'pythia':{}}
compiledData['v+jets']['>lo']={'minnlo':{},'fxfx':{}}

compiledData['tt+jets']={'nlo':{}}
compiledData['tt+jets']['nlo']={'powheg':{},'openloops':{},'fxfx':{}}

compiledData['ttbb']={'nlo':{}}
compiledData['ttbb']['nlo']={'openloops':{}}

compiledData['b_bbar_4l']={'nlo':{}}
compiledData['b_bbar_4l']['nlo']={'powheg':{}}

compiledData['tt+jets+no_ttbb']={'nlo':{}}
compiledData['tt+jets+no_ttbb']['nlo']={'powheg':{},'fxfx':{}}

compiledData['tt+jets+XX']={'nlo':{}}
compiledData['tt+jets+XX']['nlo']={'powheg':{},'fxfx':{}}

compiledData['ttv']={'lo':{},'nlo':{}}
compiledData['ttv']['lo']={'mlm':{}}
compiledData['ttv']['nlo']={'fxfx':{},'amcatnlo':{}}

compiledData['st']={'lo':{},'nlo':{}}
compiledData['st']['lo']={'comphep':{}}
compiledData['st']['nlo']={'powheg':{},'amcatnlo':{}}

compiledData['vv']={'lo':{},'nlo':{}}
compiledData['vv']['lo']={'madgraph':{},'pythia':''}
compiledData['vv']['nlo']={'powheg':{},'amcatnlo':{},'fxfx':{}}

compiledData['multijet']={'lo':{}}
compiledData['multijet']['lo']={'madgraph':{},'pythia':{},'mlm':{}}

compiledData['gamma+jets']={'lo':{}}
compiledData['gamma+jets']['lo']={'mlm':{}}

#   ----------------------------------------------------- #

# updating the compiledData with nthe data colums

headList=list(compiledData.keys())
for head in headList:
    compiledData[head][head+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
    kysList=list(compiledData[head].keys())
    for kys in kysList:
        if kys not in tires:
            continue
        compiledData[head][kys+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
        for kkys in compiledData[head][kys]:
            compiledData[head][kys][kkys]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
        

#compiledData={}
#for head in heads:
#    compiledData[head]={}
#    compiledData[head][head+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
#    compiledData[head]['lo']   = {'pythia':{},'madgraph':{},'mlm':{},'pythiamlm':{},'madgraphmlm':{}}
#    #compiledData[head]['lo']   = {'pythia':{},'madgraph':{}}
#    compiledData[head]['nlo']     = {'openloops':{},'powheg':{},'amcatnlo':{},'herwig':{},'fxfx':{},'photos':{}}
#    #compiledData[head]['nlo']     = {'powheg':{},'amcatnlo':{},'fxfx':{}}
#    compiledData[head]['nnlo']    = {'minnlo':{}}
#    #compiledData[head]['nnlo']    = {}
#    #compiledData[head]['>lo']     = compiledData[head]['nlo'].copy() ; compiledData[head]['>lo'].update(compiledData[head]['nnlo']);
#    for kys in tires:
#        compiledData[head][kys+'_all']={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
#        for kkys in compiledData[head][kys]:
#            compiledData[head][kys][kkys]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}

compiledGeneratorStats={}
for head in compiledTags:
    compiledGeneratorStats[head]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}

HTBins=['70to100','100to200','200to400','400to600','600to800','800to1200','1200to2500']
compiledHTBinStats={}
for head in HTBins:
    compiledHTBinStats[head]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}


compiledPOGStats={}


def updateCompiledStats( stats,compiledData ):
    compiledData['totalEvents']+=stats['events']
    compiledData['totalCpuSec']+=stats['cpuTime']
    compiledData['prepids'].append(stats['prepid'])
    compiledData['datasets'].append(stats['dataset'])
    if compiledData['totalEvents'] > 0 :
        compiledData['cpuSecPerEvent'] = compiledData['totalCpuSec']/compiledData['totalEvents']
        compiledData['hs06']           = compiledData['cpuSecPerEvent']*HSO6_CONVERSION_FACTOR

def compileStats( stats,cStats,tag):
    toBeAdded=False
    for preci in cStats[tag]:
        if preci not in tires:
            continue
        isPreci=False
        for genMachine in cStats[tag][preci]:
            isPreci = isPreci or stats[genMachine]
            if stats[genMachine]:
                updateCompiledStats(stats,cStats[tag][preci][genMachine])
        if isPreci:
            updateCompiledStats(stats,cStats[tag][preci+'_all'])
        toBeAdded = toBeAdded or isPreci
    if toBeAdded:
        updateCompiledStats(stats,cStats[tag][tag+'_all'])

tabS="  "

def printDetailsOfItem(cTag,compiledStats):
    
    idxs=np.argsort(compiledStats['datasets'])
    
    print("\n")
    fstring=(" ~ ~   "+cTag+"  ("+str(len(idxs))+" prepids)   ~ ~").center(81)
    print("".center(len(fstring),"-"))
    print(fstring)
    print("".center(len(fstring),"-"))
    
    idxs=np.argsort(compiledStats['datasets'])
    i=0
    for idx in idxs:
        i+=1
        fstring=str(i).ljust(3)+" , "+compiledStats['datasets'][idx].ljust(60)+" ( "
        fstring+=compiledStats['prepids'][idx].center(30)+" )"
        print(fstring)
 
def printLinearTable(compiledData,printTagExp=False,printDetails=False):
    fstring  ="|"+"TAG".center(20)+" | "
    fstring +="Total Events [1e6]".rjust(18)+" | "
    fstring +="Total cpu s [1e9]".rjust(18)+" | "
    fstring +="Total cpu s/evt".rjust(18)+" | "
    fstring +="HS06".center(18)+" | "
    if(printTagExp):
        fstring +="Remarks".center(30) + " |"
    print("".center(len(fstring),"-"))
    print(fstring)
    print("".center(len(fstring),"-"))
    for tag in compiledData:
        if compiledData[tag]['totalEvents']<1:
            continue
        fstring  ="|"+(tabS+tag).ljust(20)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag]['totalEvents']/1e6).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag]['totalCpuSec']/1e9).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag]['cpuSecPerEvent']).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag]['hs06']).rjust(18)+" | "
        if(printTagExp):
            fstring +=compiledTags[tag].center(30) + " |"
        print(fstring)
    print("".center(len(fstring),"-"))
    print("")
    if not printDetails:
        return
    for tag in compiledData:
        if compiledData[tag]['totalEvents']<1:
            continue
        printDetailsOfItem(tag,compiledData[tag])
     
def printTableOfCompiledData(compiledData,printDetails=False):
    fstring  ="|"+"TAG".center(20)+" | "
    fstring +="Total Events [1e6]".rjust(18)+" | "
    fstring +="Total cpu s [1e9]".rjust(18)+" | "
    fstring +="Total cpu s/evt".rjust(18)+" | "
    fstring +="HS06".center(18)+" | "
    fstring +="Remarks".center(30) + " |"
    print("".center(len(fstring),"-"))
    print(fstring)
    print("".center(len(fstring),"-"))
    
    for tag in compiledData:
        if compiledData[tag][tag+'_all']['totalEvents']<1:
            continue
        fstring  ="|"+(tabS+tag).ljust(20)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag][tag+'_all']['totalEvents']/1e6).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag][tag+'_all']['totalCpuSec']/1e9).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag][tag+'_all']['cpuSecPerEvent']).rjust(18)+" | "
        fstring +="{0:0.2f}".format(compiledData[tag][tag+'_all']['hs06']).rjust(18)+" | "
        fstring +=compiledTags['all'].center(30) + " |"
        print(fstring)
        for preci in compiledData[tag]:
            if preci not in tires:
                continue
            if compiledData[tag][preci+'_all']['totalEvents']<1:
                continue
            fstring  ="|"+(tabS*2+preci).ljust(20)+" | "
            fstring +="{0:0.2f}".format(compiledData[tag][preci+'_all']['totalEvents']/1e6).rjust(18)+" | "
            fstring +="{0:0.2f}".format(compiledData[tag][preci+'_all']['totalCpuSec']/1e9).rjust(18)+" | "
            fstring +="{0:0.2f}".format(compiledData[tag][preci+'_all']['cpuSecPerEvent']).rjust(18)+" | "
            fstring +="{0:0.2f}".format(compiledData[tag][preci+'_all']['hs06']).rjust(18)+" | "
            fstring +=compiledTags[preci].center(30) + " |"
            print(fstring)
        
            for genMachine in compiledData[tag][preci]:
                if compiledData[tag][preci][genMachine]['totalEvents'] <1 :
                    continue
                fstring  ="|"+(tabS*3+genMachine).ljust(20)+" | "
                fstring +="{0:0.2f}".format(compiledData[tag][preci][genMachine]['totalEvents']/1e6).rjust(18)+" | "
                fstring +="{0:0.2f}".format(compiledData[tag][preci][genMachine]['totalCpuSec']/1e9).rjust(18)+" | "
                fstring +="{0:0.2f}".format(compiledData[tag][preci][genMachine]['cpuSecPerEvent']).rjust(18)+" | "
                fstring +="{0:0.2f}".format(compiledData[tag][preci][genMachine]['hs06']).rjust(18)+" | "
                fstring +=compiledTags[genMachine].center(30) + " |"
                print(fstring)
    print("".center(len(fstring),"-"))
    print("\n")
    if not printDetails:
        return
    
       
    
    for tag in compiledData:
        if compiledData[tag][tag+'_all']['totalEvents'] <1:
            continue
        printDetailsOfItem(tag+"_all",compiledData[tag][tag+'_all']);
        for preci in compiledData[tag]:
            if preci not in tires:
                continue
            if compiledData[tag][preci+'_all']['totalEvents']<1:
                continue
            printDetailsOfItem(tag+"_"+preci+"_all",compiledData[tag][preci+'_all']);
            for genMachine in compiledData[tag][preci]:
                if compiledData[tag][preci][genMachine]['totalEvents'] <1 :
                    continue
                printDetailsOfItem(tag+"_"+preci+"_"+genMachine,compiledData[tag][preci][genMachine]);
    



stats={}

tot_kevt=0
tot_cpu_ksec =0

for line in Lines:
    if line.startswith("#") is False:
        split_strings = line.split()    
        pid = split_strings[1].strip()
    else:
        continue
    pog=pid[:3]
 #   print(doAllPogs,"|",pog,"|",POG,"|",pog!=POG,not  doAllPogs and pog!=POG)
    if( not  doAllPogs and pog!=POG): continue
 #   print(" doing pid  :  " ,pid)
    if dataMode=="rest":
        print("doing  : ",pid)
        res=get_request(pid)
    elif dataMode=="json":
        res = data[pid]
    
    res = [res]
    for r in res:
        stats[pid]={}
        if pid in exception_prepids:    
            split_strings.insert(19,"?????????? | ???????") 
         #elif "SUS-RunIISummer20UL18wmLHEGEN-00044" not in pid and "EXO-RunIISummer20UL18wmLHEGEN-00130" not in pid and "SUS-RunIISummer20UL18GEN-00013" not in pid: 
         #elif "SUS-RunIISummer20UL18wmLHEGEN-00044" not in pid and "EXO-RunIISummer20UL18wmLHEGEN-00130" not in pid and "SUS-RunIISummer20UL18GEN-00013" not in pid: 
        else:
            split_strings.insert(19,r['dataset_name'])
            split_strings.insert(20,"")
            final_string = ' '.join(split_strings)
 
        
            stats[pid]['dataset'] = r['dataset_name']
            stats[pid]['prepid']  = pid
            stats[pid]['events']         = int(split_strings[3])*1000
            stats[pid]['cpuPerEvent']     = float(split_strings[5])
            stats[pid]['cpuPerSimEvent']     = float(split_strings[9])
            stats[pid]['initTime']         = float(split_strings[13])
            stats[pid]['cpuTime']         = float(split_strings[15])*1e3
            stats[pid]['hs06']          = HSO6_CONVERSION_FACTOR*stats[pid]['cpuTime']/stats[pid]['events']

            dsetname= stats[pid]['dataset'].lower()
   
            if 'herwig' in dsetname:     stats[pid]['herwig']=True
            else:  stats[pid]['herwig']=False
        
            if 'minnlo' in dsetname:     stats[pid]['minnlo']=True
            else :                      stats[pid]['minnlo']=False        
                
            if 'comphep' in dsetname:     stats[pid]['comphep']=True
            else :                      stats[pid]['comphep']=False        
                
            if 'openloops' in dsetname: stats[pid]['openloops']=True
            else :                      stats[pid]['openloops']=False        
                
        
            if ("powheg" in dsetname and 'openloops' not in dsetname and 'minnlo' not in dsetname) :  stats[pid]['powheg']=True
            else :                      stats[pid]['powheg']=False        
                
            if 'amcatnlofxfx' in dsetname:      stats[pid]['fxfx']=True
            else :                              stats[pid]['fxfx']=False        
        
            if ("amcatnlo" in dsetname) and ("fxfx" not in dsetname):   stats[pid]['amcatnlo']=True
            else :                                                       stats[pid]['amcatnlo']=False        
        
            x=False
            if ("amcatnlo" not in dsetname) and ("fxfx" not in dsetname) and ("powheg" not in dsetname): x=True
        
            if x and ('pythia8' in dsetname) :     stats[pid]['pythia']=True
            else :                    stats[pid]['pythia']=False
        
            if x and ('madgraph-' in dsetname or 'madgraph_' in dsetname):    stats[pid]['madgraph']=True
            else :                    stats[pid]['madgraph']=False
        
            if 'pythiamlm' in dsetname:    stats[pid]['pythiamlm']=True
            else :                stats[pid]['pythiamlm']=False
        
            if 'madgraphmlm' in dsetname:    stats[pid]['madgraphmlm']=True
            else :                stats[pid]['madgraphmlm']=False
        
            if 'mlm' in dsetname:         stats[pid]['mlm']=True
            else :                stats[pid]['mlm']=False
        
            if 'photos' in dsetname:     stats[pid]['photos']=True
            else :                stats[pid]['photos']=False
        
            if 'minnlo' in dsetname:     stats[pid]['minnlo']=True
            else :                stats[pid]['minnlo']=False
            
            if 'jhugen' in dsetname: stats[pid]['jhugen']=True
            else :                stats[pid]['jhugen'] = False

            if 'evtgen' in dsetname: stats[pid]['evtgen']=True
            else :                stats[pid]['evtgen'] = False

            if 'madspin' in dsetname: stats[pid]['madspin']=True
            else :                    stats[pid]['madspin'] = False

             
            stat=stats[pid]
            
            genList=['amcatnlo','mlm','madspin','powheg','openloops','fxfx','madgraph','madgraphmlm','pythia','pythiamlm','comphep','minnlo','photos','evtgen','jhugen'];
            for tag in genList:
                if stat[tag]:
                    updateCompiledStats(stat,compiledGeneratorStats[tag])

            pythiaOnly=True
            genList=['amcatnlo','mlm','madspin','powheg','openloops','fxfx','madgraph','madgraphmlm','pythia','pythiamlm','comphep','minnlo','photos','evtgen','jhugen'];
            for tag in genList:
                if tag=='pythia':
                    pythiaOnly = pythiaOnly and stat[tag]
                else:
                    pythiaOnly = pythiaOnly and (not stat[tag])
            if pythiaOnly:
                updateCompiledStats(stat,compiledGeneratorStats['pythiaOnly'])
            
           # if stat['amcatnlo'] :    updateCompiledStats(stat,compiledGeneratorStats['amcatnlo'])
           # if stat['mlm'] :    updateCompiledStats(stat,compiledGeneratorStats['mlm'])
           # if stat['powheg'] :    updateCompiledStats(stat,compiledGeneratorStats['powheg'])
           # if stat['openloops'] :    updateCompiledStats(stat,compiledGeneratorStats['openloops'])
           # if stat['fxfx'] :    updateCompiledStats(stat,compiledGeneratorStats['fxfx'])
           # if stat['madgraph'] :    updateCompiledStats(stat,compiledGeneratorStats['madgraph'])
           # if stat['madgraphmlm']:    updateCompiledStats(stat,compiledGeneratorStats['madgraphmlm'])
           # if stat['pythia'] :    updateCompiledStats(stat,compiledGeneratorStats['pythia'])
           # if stat['pythiamlm'] :    updateCompiledStats(stat,compiledGeneratorStats['pythiamlm'])
           # if stat['comphep'] :    updateCompiledStats(stat,compiledGeneratorStats['comphep'])
           # if stat['minnlo'] :    updateCompiledStats(stat,compiledGeneratorStats['minnlo'])
           # if stat['photos'] :    updateCompiledStats(stat,compiledGeneratorStats['photos'])
            
    #        pog=pid[:3]
            if pog not in compiledPOGStats:
                compiledPOGStats[pog]={'prepids':[],'datasets':[],'totalEvents' : 0, 'totalCpuSec' :0 , 'cpuSecPerEvent' : -1,'hs06':-1}
	    
            updateCompiledStats(stat,compiledPOGStats[pog])
            compileStats(stat,compiledDataPOG,pog)


            if dsetname.startswith('wjetstolnu_ht'):
                for head in compiledHTBinStats:
                    if head in dsetname:
                        updateCompiledStats(stat,compiledHTBinStats[head])

            if dsetname.startswith('ttz') or dsetname.startswith('ttw'):
                compileStats(stat,compiledData,'ttv')        
            if dsetname.startswith("st_"):
                compileStats(stat,compiledData,'st')        
            
            if ( ("ww" in dsetname) or ("wz" in dsetname) or ("zz" in dsetname) ) and ( ("hto" not in dsetname) \
                and ("glugluto" not in dsetname) and ("higgs" not in dsetname) and ("twz" not in dsetname) ): 
                compileStats(stat,compiledData,'vv')
        
            if ( dsetname.startswith("wjets") ) \
                or ("dytohpphmm" not in dsetname and dsetname.startswith("dy")) \
                or ("usjets" in dsetname) or( dsetname.startswith("w") and "jets" in dsetname):
                compileStats(stat,compiledData,'v+jets')
        
            if ("ttjets" in dsetname)  or ('tttosemilep' in dsetname) or ('tttohadro' in dsetname)\
                or ('ttbb' in dsetname):
                    compileStats(stat,compiledData,'tt+jets')
            
            if ( ("ttjets" in dsetname)  or ('tttosemilep' in dsetname) or ('tttohadro' in dsetname) )\
                and ('ttbb' not in dsetname):
                compileStats(stat,compiledData,'tt+jets+no_ttbb')
            
            if (("ttjets" in dsetname)  or ('tttosemilep' in dsetname) or ('tttohadro' in dsetname))\
                 and ('ttbb' not in dsetname) and ('ht500njet' not in dsetname):
                compileStats(stat,compiledData,'tt+jets+XX')
            if ("ttbb" in dsetname):
                compileStats(stat,compiledData,'ttbb')
            if ("b_bbar_4l" in dsetname):
                compileStats(stat,compiledData,'b_bbar_4l')
                
            if dsetname.startswith("qcd"):
                compileStats(stat,compiledData,'multijet')
                
            if (dsetname.startswith("gjets")):
                compileStats(stat,compiledData,'gamma+jets')

#print("POG Stats : \n")
#printLinearTable(compiledPOGStats,printTagExp=False,printDetails=False)
#print("\n\n\n")

print("Generator Stats :\n")
printLinearTable(compiledGeneratorStats,printTagExp=False,printDetails=False)
print("\n\n\n")

#print("Sample Stats : \n")
#printTableOfCompiledData(compiledDataPOG,False)    
#print("\n\n\n")
#            
#print("Summary for standard configurations: HT-binned WJets MG5_aMC [MLM] \n")
#printLinearTable(compiledHTBinStats,printTagExp=False,printDetails=False)
#print("\n\n\n")


if FULL_DETAILS:
   print("\n\n<==================>     FULL DETAILS OF SAMPLES USED FOR CLACULATIONS <==================>\n\n")
   #print("POG Stats : \n")
   #printLinearTable(compiledPOGStats,False,printDetails=True)
   #print("\n\n\n")
   #
   print("Generator Stats :\n")
   printLinearTable(compiledGeneratorStats,False,printDetails=True)
   print("\n\n\n")
   
#   print("Sample Stats : \n")
#   printTableOfCompiledData(compiledDataPOG,printDetails=True)    
#   print("\n\n\n")
#               
#   print("Summary for standard configurations: HT-binned WJets MG5_aMC [MLM] \n")
#   printLinearTable(compiledHTBinStats,False,printDetails=True)
#   print("\n\n\n")

