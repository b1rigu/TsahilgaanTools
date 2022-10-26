from pick import pick
import math


def activeResXInput():
    s = float(input('input S [kVA]: ')) * 1000
    Vth = float(input('input Vth [kV]: ')) * 1000
    Vtl = float(input('input Vtl [kV]: ')) * 1000
    Poc = float(input('input Poc [kW]: ')) * 1000
    Psc = float(input('input Psc [kW]: ')) * 1000
    Uscpercent = float(input('input Usc [%]: ')) / 100
    Iocpercent = float(input('input Ioc [%]: ')) / 100
    return s, Vth, Vtl, Poc, Psc, Uscpercent, Iocpercent


def activeResXCalculation(s, Vth, Vtl, Poc, Psc, Uscpercent, Iocpercent):
    Rth = (Psc * Vth**2) / s**2
    Rtl = (Psc * Vtl**2) / s**2
    Xth = (Uscpercent * Vth**2 * 10) / s
    Xtl = (Uscpercent * Vtl**2) / s
    Gth = (Poc * 0.001) / Vth**2
    Gtl = (Poc * 0.001) / Vtl**2
    Bth = (Iocpercent * s) / Vth**2
    Btl = (Iocpercent * s) / Vtl**2
    return Rth, Rtl, Xth, Xtl, Gth, Gtl, Bth, Btl


def activeResX():
    s, Vth, Vtl, Poc, Psc, Uscpercent, Iocpercent = activeResXInput()
    Rth, Rtl, Xth, Xtl, Gth, Gtl, Bth, Btl = activeResXCalculation(
        s, Vth, Vtl, Poc, Psc, Uscpercent, Iocpercent)
    print(f'''
---------------------------Hariu!---------------------------     
    Rth = {'{:.4g}'.format(Rth)}, Rtl = {'{:.4g}'.format(Rtl)}
    Xth = {'{:.4g}'.format(Xth)}, Xtl = {'{:.4g}'.format(Xtl)}
    Gth = {'{:.4g}'.format(Gth)}, Gtl = {'{:.4g}'.format(Gtl)}
    Bth = {'{:.4g}'.format(Bth)}, Btl = {'{:.4g}'.format(Btl)}
---------------------------Hariu!---------------------------''')


def tusulTootsoo():
    print('------------------------Tusul tootsoo------------------------')
    shugamuudiinToo = int(input('heden shugam baigaa ve: '))
    shugamuud = []
    pmaxUtguud = []
    shugmaiinUrtuud = []
    hereglegchid = {}
    lastP_value = 0
    PehlelUtguud = []

    for i in range(shugamuudiinToo):
        print(
            f'------------------------{i + 1}-r Shugam------------------------')
        shugam = []
        shugam.append(input('?? ees ? hurtelh shugam. ?? ni: ').upper())
        shugam.append(
            input(f'{shugam[0]} ees ? hurtelh shugam. ? ni: ').upper())
        shugamuud.append(shugam)

    for i in shugamuud:
        hereglegchid[i[0]] = []
        hereglegchid[i[1]] = []

    for stantsName in hereglegchid.keys():
        print(
            f'------------------------{stantsName}-r Hereglegch------------------------')
        ugugdul = []
        ugugdul.append(float(input('input X [mm]: ')))
        ugugdul.append(float(input('input Y [mm]: ')))
        if (stantsName != 'C'):
            ugugdul.append(float(input('input Pmax [MW]: ')))
            ugugdul.append(float(input('input cosf: ')))
        hereglegchid[stantsName] = ugugdul

    print('------------------------Hariu--------------------------')
    for shugam in shugamuud:
        xi = hereglegchid.get(shugam[0])[0]
        yi = hereglegchid.get(shugam[0])[1]
        xj = hereglegchid.get(shugam[1])[0]
        yj = hereglegchid.get(shugam[1])[1]
        m = 2.6
        L = m * math.sqrt((xi - xj)**2 + (yi - yj)**2)
        shugmaiinUrtuud.append(L)
        print(f'L({shugam[0]} - {shugam[1]}) [km] = {"{:.4g}".format(L)}')

    for shugamName in hereglegchid.keys():
        if 2 < len(hereglegchid.get(shugamName)):
            Pmax = hereglegchid.get(shugamName)[2]
            p10jil = Pmax * 1.03
            pmaxUtguud.append(p10jil)
            print(f'p({shugamName}) 10jil [MW] = {p10jil}')

    for i in range(len(shugamuud) - 1, -1, -1):
        Pe = (pmaxUtguud[i] + lastP_value) * 0.05 + pmaxUtguud[i] + lastP_value
        PehlelUtguud.append(Pe)
        U = 4.35 * math.sqrt(shugmaiinUrtuud[i] + 16 * Pe)
        lastP_value = Pe
        print(f'Pe({shugamuud[i][0]} - {shugamuud[i][1]}) [MW] = {Pe}')
        print(f'Usongoh({shugamuud[i][0]} - {shugamuud[i][1]}) [kV] = {U}')


title = 'Please choose: '
options = [
    'Activ eserguutsel, damjuulamj todorhoiloh',
    'Tosliin tootsoo']
option, index = pick(options, title, indicator='=>')

if index == 0:
    activeResX()
elif index == 1:
    tusulTootsoo()
