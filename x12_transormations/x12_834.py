def transform_834(msg):
    strip_msg = msg.strip().split('~')

    sender_id= (strip_msg[1].split('*'))[2]
    receiver_id= (strip_msg[1].split('*'))[3]
    
    print(sender_id)
    print(receiver_id)
    

msg = """ISA*00*          *00*          *ZZ*UHC           *ZZ*ASHHEALTH      *240719*0810*^*00501*000000906*1*T*:~
GS*BE*UHC*ASHHEALTH*20240719*0810*2*X*005010X220A1~
ST*834*0002~
BGN*00*ENROLL20240719*20240719*0810*PT**4~

INS*Y*18*030*XN*A*E**FT~
REF*0F*M987654321~                       ← Subscriber/member ID
REF*1L*PLAN456~                          ← Group or plan number
DTP*356*D8*20240715~                     ← Coverage effective date

NM1*IL*1*SMITH*JOHN****34*987654321~     ← Subscriber name and ID
DMG*D8*19791111*M~                       ← DOB and gender

HD*030**HLT*PLAN456~                     ← Health coverage type and plan ID
DTP*348*D8*20240715~                     ← Benefit coverage start
DTP*349*D8*20241231~                     ← Benefit coverage end

SE*13*0002~
GE*1*2~
IEA*1*000000906~
"""

transform_834(msg)