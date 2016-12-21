import os, sys, subprocess, re

if len(sys.argv) < 1:
    print("Need output device")
    exit()

jkl = 'pacmd list-sinks | egrep "index:|alsa.name"'
asd = str(subprocess.check_output(jkl, shell=True))[2:]
kk = re.split('index: ', asd)

kk.remove(kk[0])

outputs = {'HDMI': '', 'head': ''}

for item in kk:
    if "HDMI" in item:
        outputs['HDMI'] = item[:item.find('\\')]
    elif "USB" in item:
        outputs['head'] = item[:item.find('\\')]

arg1 = sys.argv[1]
mno = "pacmd list-sink-inputs | grep 'index'"
pqr = str(subprocess.check_output(mno, shell=True))[2:]
lkn = re.split('index: ', pqr)
lkn.remove(lkn[0])

inputs = []
for input in lkn:
    inputs.append(input[:input.find('\\')])

if arg1.lower() == 'h':
    cmd = "pacmd set-default-sink %s" % outputs['head']
    os.system(cmd)
    for input in inputs:
        cmd2 = "pacmd move-sink-input %s %s" % (input, outputs['head'])
        os.system(cmd2)
elif arg1.lower() == 's':
    cmd = "pacmd set-default-sink %s" % outputs['HDMI']
    os.system(cmd)
    for input in inputs:
        cmd2 = "pacmd move-sink-input %s %s" % (input, outputs['HDMI'])
        os.system(cmd2)

print("Done.")