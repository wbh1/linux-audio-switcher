import os, sys, subprocess, re
import config

if len(sys.argv) < 1:
    print("Need output device")
    exit()

jkl = 'pacmd list-sinks | egrep "index:|alsa.name"'
asd = str(subprocess.check_output(jkl, shell=True))[2:]
kk = re.split('index: ', asd)

kk.remove(kk[0])

outputs = {'1': '', '2': ''}

for item in kk:
    if config.input1 in item:
        outputs['1'] = item[:item.find('\\')]
    elif config.input2 in item:
        outputs['2'] = item[:item.find('\\')]

arg1 = sys.argv[1]
mno = "pacmd list-sink-inputs | grep 'index'"
pqr = str(subprocess.check_output(mno, shell=True))[2:]
lkn = re.split('index: ', pqr)
lkn.remove(lkn[0])

inputs = []
for input in lkn:
    inputs.append(input[:input.find('\\')])

if arg1.lower() == 'h':
    cmd = "pacmd set-default-sink %s" % outputs['2']
    os.system(cmd)
    for input in inputs:
        cmd2 = "pacmd move-sink-input %s %s" % (input, outputs['2'])
        os.system(cmd2)
elif arg1.lower() == 's':
    cmd = "pacmd set-default-sink %s" % outputs['1']
    os.system(cmd)
    for input in inputs:
        cmd2 = "pacmd move-sink-input %s %s" % (input, outputs['1'])
        os.system(cmd2)

print("Done.")