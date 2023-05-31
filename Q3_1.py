import json 
hai = {
"""1) in which continent is Russia located ?
a.Asia
b.Europe
""":"b",
"""2) in which continent is Syria located ?
a.Asia
b.Europe
""":"a",
"""3) in which continent is Spain located ?
a.Asia
b.Europe
""":"b",
"""4) in which continent is Iraq located ?
a.Asia
b.Europe
""":"a",
"""5) in which continent is Jordan located ?
a.Asia
b.Europe
""":"a",
"""6) in which continent is France located ?
a.Asia
b.Europe
""":"b",
"""7) in which continent is Italy located ?
a.Asia
b.Europe
""":"b",
"""8) in which continent is Lebanon located ?
a.Asia
b.Europe
""":"a",
"""9) in which continent is Iran located ?
a.Asia
b.Europe
""":"a",
"""10) in which continent is India located ?
a.Asia
b.Europe
""":"a",
"""11) in which continent is Portugal located ?
a.Asia
b.Europe
""":"b",
"""12) in which continent is Austria located ?
a.Asia
b.Europe
""":"b",
"""13) in which continent is Holland located ?
a.Asia
b.Europe
""":"b",
"""14) in which continent is Germany located ?
a.Asia
b.Europe
""":"b",
"""15) in which continent is UAE located ?
a.Asia
b.Europe
""":"a",
"""16) in which continent is Qatar located ?
a.Asia
b.Europe
""":"a",
"""17)in which continent is yemen located ?
a.Asia
b.Europe
""":"a",
"""18) in which continent is Denmark located ?
a.Asia
b.Europe
""":"b",
"""19) in which continent is Kuwait located ?
a.Asia
b.Europe
""":"a",
"""20) in which continent is Croatia located ?
a.Asia
b.Europe
""":"b",
}
haidara=json.dumps(hai)
with open("haidara.json","w")as f:
    f.write(haidara)
