"""mod1"""
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sympy import pprint, Symbol
import numpy as np

arr = np.array([])


class ConductionExperiments:

    '''Programs to find the Results of conduction based experiments '''

    def __init__(self, Burrete_reading: type(np.ndarray | None), lube_reading: type(np.ndarray | None), water_reading: type(np.ndarray | None)) -> None:

        self.Burrete_reading = Burrete_reading
        self.lube_reading = lube_reading
        self.water_reading = water_reading

        global arr
        arr = np.array([])
        arr = np.array(Burrete_reading, dtype=float)
        self.arr = arr

    def hardness(self):
        '''program to find hardness of water'''
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                x = Symbol('Weight of EDTA x4')
                y = Symbol('Molecular weight of EDTA(372.14)')
                print('Molarity of EDTA = \n')
                pprint(x / y)

                W1 = float(
                    input('Weight of the bottle + disodium salt of EDTA (W1) = '))
                W2 = float(input('Weight of the bottle (W2) = '))
                W_EDTA = W1-W2
                print("Weight of di sodium salt of EDTA = %.4f" % W_EDTA)
                warnings.filterwarnings("ignore")

                Mol_EDTA = round((W_EDTA*4)/372.14, 4)

                print('Molarity of EDTA = %.4f' % Mol_EDTA)
                in_Burrete_reading = arr
                for i in range(len(arr)):
                    in_Burrete_reading[i, 0] = in_Burrete_reading[i,
                                                                  0] + in_Burrete_reading[i, 1]

                in_Burrete_reading = np.delete(in_Burrete_reading, 1, 1)
                in_Burrete_reading = np.mean(in_Burrete_reading, axis=0)

                print('CALCULATIONS  : \n')
                pprint(
                    'Volume of EDTA = 13 cm³ \n1000cm³ 1M EDTA = 100g (Molecular mass of CaCO₃ = 100)\n\n')
                pprint('13 cm³ of %.4fM of EDTA = ' % (Mol_EDTA))
                x = round(in_Burrete_reading[0], 4)*Mol_EDTA*100
                y = 100
                caco3 = round(x/y, 4)
                print('%.4fg of CaCO₃ \n' % caco3)

                Total_hardness = (caco3*(10**5))/25

                pprint('Total hardness of given water(25cm³) sample = %.2f ppm of CaCO₃' % (
                    Total_hardness))

        except ZeroDivisionError:
            print('W-?-!--0--!---')
        finally:
            print('=======================')

    def Chemical_Oxygen_Demand(self):
        '''program to calculate Oxygen demand'''
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                x = Symbol('Weight of Mohr\'s salt x4')
                y = Symbol('Molecular weight of Mohr\'s salt (372.14)')
                pprint(x/y)

                W1 = float(input('\nWeight of the bottle + FAS (W1) = '))
                W2 = float(input('Weight of the bottle (W2) = '))
                W_FAS = W1-W2
                print("Weight of di sodium salt of EDTA = %.4f" % W_FAS)
                warnings.filterwarnings("ignore")

                Norma_FAS = round((W_FAS*4)/392.14, 4)

                print('\nMolarity of EDTA = %.4f' % Norma_FAS)
                in_Burrete_reading = arr
                for i in range(len(arr)):
                    in_Burrete_reading[i] = round(
                        (in_Burrete_reading[i, 0] + in_Burrete_reading[i, 1]), 5)

                in_Burrete_reading = np.delete(in_Burrete_reading, 1, 1)

                in_Burrete_reading = np.mean(in_Burrete_reading, axis=0)

                print('\nCALCULATIONS  : \n')
                print(f'volume of FAS consumed = {in_Burrete_reading[0]} \n')
                blank_Titrate_Value = float(
                    input('Enter the Blank titrate value : '))
                pprint(
                    '''\n100cm³ of 1N Mohrs salt solution = 1 equivalent of oxygen\n\t\t\ti.e, 8g of Oxygen\n\n''')

                COD = round(
                    (8*(in_Burrete_reading[0]-blank_Titrate_Value)*Norma_FAS*1000)/25, 5)

                pprint('COD of {0}cm³ of {1}N of Mohr\'s salt solution is {2}mg of oxygen/cm³'.format(
                    blank_Titrate_Value, Norma_FAS, COD))

        except ZeroDivisionError:
            print('W-?-!--0--!---')
        finally:
            print('=======================')

    def Iron_in_TMT(self):
        '''program to Estimate percent of iron in TMT bar'''
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                x = Symbol('Weight of Potassium Dichromate x4')
                y = Symbol('Molecular weight of Potassium Dichromate (49)')
                pprint(x/y)

                W1 = float(
                    input('\nWeight of the bottle + Potassium Dichromate (W1) = '))
                W2 = float(input('Weight of the bottle (W2) = '))
                W_KCr = W1-W2
                print("Weight of di sodium salt of EDTA = %.4f" % W_KCr)
                warnings.filterwarnings("ignore")

                Norma_KCr = round((W_KCr*4)/49, 5)

                print('\nMolarity of EDTA = %.4f' % Norma_KCr)
                in_Burrete_reading = arr
                for i in range(len(arr)):
                    in_Burrete_reading[i] = in_Burrete_reading[i,
                                                               0] - in_Burrete_reading[i, 1]

                in_Burrete_reading = np.delete(in_Burrete_reading, 1, 1)

                in_Burrete_reading = np.mean(in_Burrete_reading, axis=0)

                print('\nCALCULATIONS  : \n')
                print(
                    f'volume of Potassium Dichromate consumed = {in_Burrete_reading[0]} \n')
                W_TMT = float(
                    input('Enter the weight of given TMT bar in 250cm³ of solution : '))

                cal = round(((55.8*in_Burrete_reading[0])*Norma_KCr)/1000, 5)

                print('\n{0}cm³ of {1}N of Potassium Dichromate solution is {2}g of Fe'.format(
                    in_Burrete_reading[0], Norma_KCr, cal))

                TMT = round((cal*1000)/W_TMT, 5)

                pprint(
                    'Percentage of iron in the given 250g of TMT bar solution is {0}%'.format(TMT))

        except ZeroDivisionError:
            print('W-?-!--0--!---')
        finally:
            print(
                '=============================================================================')

    def Viscosity(self):
        '''program to Determine Viscosity coefficient of Lubricant'''
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                x = Symbol('n₁t₂d₂')
                y = Symbol('t₁d₁')
                pprint(x/y)

                water_Average = round(np.mean(self.water_reading), 5)
                Lube_Average = round(np.mean(self.lube_reading), 5)
                warnings.filterwarnings("ignore")

                lab_temp = float(input('Enter the lab temprature : '))
                Lubricant_number = int(input('Enter the lubricant number : '))

                print('\nCALCULATIONS : \n')

                Visco_Water = float(
                    input('\nEnter the Viscosity coefficient of water(n₁) : '))
                Density_Water = float(
                    input('Enter the density of water(d₁) : '))
                Density_lube = float(input('Enter the density of lube(d₂) : '))

                visco_lube = round(
                    ((Visco_Water*Lube_Average*Density_lube)/(water_Average*Density_Water)), 5)

                print(
                    f'\nThe Viscisity coefficient of liven lubricant at {lab_temp}°C is {visco_lube} millipoise')

        except ZeroDivisionError:
            print('W-?-!--0--!---')
        finally:
            print(
                '=============================================================================')

    @staticmethod
    def Estimation_of_Copper(volume: type = np.ndarray, Optical_Density: type = np.ndarray):
        '''program to Estimate Copper present in Electroplatting Effluent'''

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            print('\nCSOLUTION  : \n')

            Vol_Sol = float(input('Enter the Volume of the solution : '))
            print(
                f'{Vol_Sol}ml of test solution contains {Vol_Sol}x4 = {Vol_Sol*4}mg of CuSO₄.5H₂O (Y)')
            print('249.65g of CuSO₄.5H₂O contains 63.54g of Cu')

            pprint('\nY mg of CuSO₄ contains : \n')
            pprint(Symbol('63 x Y')/Symbol('249.65'))
            sol = round(((63.54*Vol_Sol*4)/249.65), 5)
            print('\t\t\t={0}mg of copper'.format(sol))

            plt.plot(volume, Optical_Density, label='vol-OD', color='#1442cc')
            plt.scatter(volume, Optical_Density, color='#ff6600')
            plt.xticks(volume)
            plt.legend()
            plt.grid()
            plt.show()


class PotentiometricConductionExperiments:
    def __init__(self) -> None:
        pass

    @classmethod
    def p_Ka(cls, file_name: str, x_ax1: float, x_ax2: float, y_ax: float):
        '''Program to find pKa'''
        dat_frame = pd.read_csv(file_name)  # 'sample.csv'

        Frame = plt.figure()
        Frame.set_figwidth(18)
        Frame.set_figheight(8)

        plt.plot(dat_frame['volume'], dat_frame['pH'])
        plt.plot([x_ax1]*20, np.arange(0, 10.0, 0.5),
                 label='Calculated solution')  # 6
        plt.plot([x_ax2]*12, np.arange(0, 6, 0.5), color='magenta')  # 3
        plt.plot(np.arange(0, 5, 0.5), [y_ax]*10,
                 label='pKa', color='magenta')  # 4.75

        plt.xticks(dat_frame['volume'])
        plt.show()

        Frame = plt.figure()
        Frame.set_figwidth(20)
        Frame.set_figheight(7)

        plt.plot([6]*7, np.arange(0, 3.5, 0.5))

        plt.plot(dat_frame['volume'], dat_frame['DelpH'], label='Devation',
                 linestyle='-.', color='red', marker='*', markeredgecolor='blue')
        plt.xticks(dat_frame['volume'])
        plt.legend()
        plt.show()


# g = ConductionExperiments()
# g.pKa('E:\\RLJIT\\SEM_2\\chemistry\\Project\\sample.csv', 6, 3, 4.75)
