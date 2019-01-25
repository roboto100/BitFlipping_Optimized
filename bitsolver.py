import random
import math

# The next 1000 or so lines are really similar functions. They handle the logic for how we should guess and what we do
# with each result. They were generated from a different python function (not handwritten).
def f1_0():
    guess = myBitSolver.guess("0")
    myBitSolver.secOnes = round((1 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f1_1,1:f1_2}
    return path[correct]()
def f1_1():
    return "1"
def f1_2():
    return "0"

def f2_0():
    guess = myBitSolver.guess("00")
    myBitSolver.secOnes = round((2 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f2_1,1:f2_2,2:f2_3}
    return path[correct]()
def f2_1():
    return "11"
def f2_2():
    guess = myBitSolver.guess("01")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f2_4,2:f2_5}
    return path[correct]()
def f2_3():
    return "00"
def f2_4():
    return "10"
def f2_5():
    return "01"

def f3_0():
    guess = myBitSolver.guess("000")
    myBitSolver.secOnes = round((3 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f3_1,1:f3_2,2:f3_3,3:f3_4}
    return path[correct]()
def f3_1():
    return "111"
def f3_2():
    guess = myBitSolver.guess("001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f3_5,2:f3_6}
    return path[correct]()
def f3_3():
    guess = myBitSolver.guess("001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f3_7,3:f3_8}
    return path[correct]()
def f3_4():
    return "000"
def f3_5():
    return "110"
def f3_6():
    guess = myBitSolver.guess("010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f3_9,2:f3_10}
    return path[correct]()
def f3_7():
    guess = myBitSolver.guess("010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f3_11,3:f3_12}
    return path[correct]()
def f3_8():
    return "001"
def f3_9():
    return "101"
def f3_10():
    return "011"
def f3_11():
    return "100"
def f3_12():
    return "010"

def f4_0():
    guess = myBitSolver.guess("0000")
    myBitSolver.secOnes = round((4 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f4_1,1:f4_2,2:f4_3,3:f4_4,4:f4_5}
    return path[correct]()
def f4_1():
    return "1111"
def f4_2():
    guess = myBitSolver.guess("0011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f4_6,3:f4_7}
    return path[correct]()
def f4_3():
    guess = myBitSolver.guess("0011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f4_8,2:f4_9,4:f4_10}
    return path[correct]()
def f4_4():
    guess = myBitSolver.guess("0011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f4_11,3:f4_12}
    return path[correct]()
def f4_5():
    return "0000"
def f4_6():
    guess = myBitSolver.guess("0001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f4_13,2:f4_14}
    return path[correct]()
def f4_7():
    guess = myBitSolver.guess("0100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f4_15,2:f4_16}
    return path[correct]()
def f4_8():
    return "1100"
def f4_9():
    guess = myBitSolver.guess("0101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f4_17,2:f4_18,4:f4_19}
    return path[correct]()
def f4_10():
    return "0011"
def f4_11():
    guess = myBitSolver.guess("0100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f4_20,4:f4_21}
    return path[correct]()
def f4_12():
    guess = myBitSolver.guess("0001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f4_22,4:f4_23}
    return path[correct]()
def f4_13():
    return "1110"
def f4_14():
    return "1101"
def f4_15():
    return "1011"
def f4_16():
    return "0111"
def f4_17():
    return "1010"
def f4_18():
    guess = myBitSolver.guess("0001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f4_24,3:f4_25}
    return path[correct]()
def f4_19():
    return "0101"
def f4_20():
    return "1000"
def f4_21():
    return "0100"
def f4_22():
    return "0010"
def f4_23():
    return "0001"
def f4_24():
    return "0110"
def f4_25():
    return "1001"

def f5_0():
    guess = myBitSolver.guess("00000")
    myBitSolver.secOnes = round((5 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_1,1:f5_2,2:f5_3,3:f5_4,4:f5_5,5:f5_6}
    return path[correct]()
def f5_1():
    return "11111"
def f5_2():
    guess = myBitSolver.guess("00011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_7,3:f5_8}
    return path[correct]()
def f5_3():
    guess = myBitSolver.guess("00011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_9,2:f5_10,4:f5_11}
    return path[correct]()
def f5_4():
    guess = myBitSolver.guess("00011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_12,3:f5_13,5:f5_14}
    return path[correct]()
def f5_5():
    guess = myBitSolver.guess("00011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f5_15,4:f5_16}
    return path[correct]()
def f5_6():
    return "00000"
def f5_7():
    guess = myBitSolver.guess("00001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_17,2:f5_18}
    return path[correct]()
def f5_8():
    guess = myBitSolver.guess("00100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_19,2:f5_20}
    return path[correct]()
def f5_9():
    return "11100"
def f5_10():
    guess = myBitSolver.guess("00101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_21,2:f5_22,4:f5_23}
    return path[correct]()
def f5_11():
    guess = myBitSolver.guess("00100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_24,3:f5_25}
    return path[correct]()
def f5_12():
    guess = myBitSolver.guess("00100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f5_26,4:f5_27}
    return path[correct]()
def f5_13():
    guess = myBitSolver.guess("00101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_28,3:f5_29,5:f5_30}
    return path[correct]()
def f5_14():
    return "00011"
def f5_15():
    guess = myBitSolver.guess("00100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f5_31,5:f5_32}
    return path[correct]()
def f5_16():
    guess = myBitSolver.guess("00001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f5_33,5:f5_34}
    return path[correct]()
def f5_17():
    return "11110"
def f5_18():
    return "11101"
def f5_19():
    return "11011"
def f5_20():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_35,2:f5_36}
    return path[correct]()
def f5_21():
    return "11010"
def f5_22():
    guess = myBitSolver.guess("01001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f5_37,2:f5_38,4:f5_39}
    return path[correct]()
def f5_23():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_40,3:f5_41}
    return path[correct]()
def f5_24():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_42,3:f5_43}
    return path[correct]()
def f5_25():
    return "00111"
def f5_26():
    return "11000"
def f5_27():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f5_44,4:f5_45}
    return path[correct]()
def f5_28():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f5_46,4:f5_47}
    return path[correct]()
def f5_29():
    guess = myBitSolver.guess("01001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f5_48,3:f5_49,5:f5_50}
    return path[correct]()
def f5_30():
    return "00101"
def f5_31():
    guess = myBitSolver.guess("01000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f5_51,5:f5_52}
    return path[correct]()
def f5_32():
    return "00100"
def f5_33():
    return "00010"
def f5_34():
    return "00001"
def f5_35():
    return "10111"
def f5_36():
    return "01111"
def f5_37():
    return "10110"
def f5_38():
    return "01110"
def f5_39():
    return "11001"
def f5_40():
    return "10101"
def f5_41():
    return "01101"
def f5_42():
    return "10011"
def f5_43():
    return "01011"
def f5_44():
    return "10100"
def f5_45():
    return "01100"
def f5_46():
    return "10010"
def f5_47():
    return "01010"
def f5_48():
    return "00110"
def f5_49():
    return "10001"
def f5_50():
    return "01001"
def f5_51():
    return "10000"
def f5_52():
    return "01000"

def f6_0():
    guess = myBitSolver.guess("000000")
    myBitSolver.secOnes = round((6 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_1,1:f6_2,2:f6_3,3:f6_4,4:f6_5,5:f6_6,6:f6_7}
    return path[correct]()
def f6_1():
    return "111111"
def f6_2():
    guess = myBitSolver.guess("000011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_8,3:f6_9}
    return path[correct]()
def f6_3():
    guess = myBitSolver.guess("000011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_10,2:f6_11,4:f6_12}
    return path[correct]()
def f6_4():
    guess = myBitSolver.guess("000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_13,2:f6_14,4:f6_15,6:f6_16}
    return path[correct]()
def f6_5():
    guess = myBitSolver.guess("000011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_17,4:f6_18,6:f6_19}
    return path[correct]()
def f6_6():
    guess = myBitSolver.guess("000011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_20,5:f6_21}
    return path[correct]()
def f6_7():
    return "000000"
def f6_8():
    guess = myBitSolver.guess("000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_22,2:f6_23}
    return path[correct]()
def f6_9():
    guess = myBitSolver.guess("001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_24,3:f6_25}
    return path[correct]()
def f6_10():
    return "111100"
def f6_11():
    guess = myBitSolver.guess("001101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_26,3:f6_27,5:f6_28}
    return path[correct]()
def f6_12():
    guess = myBitSolver.guess("001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_29,2:f6_30,4:f6_31}
    return path[correct]()
def f6_13():
    return "111000"
def f6_14():
    guess = myBitSolver.guess("001011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_32,2:f6_33,4:f6_34}
    return path[correct]()
def f6_15():
    guess = myBitSolver.guess("001011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_35,4:f6_36,6:f6_37}
    return path[correct]()
def f6_16():
    return "000111"
def f6_17():
    guess = myBitSolver.guess("001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_38,4:f6_39,6:f6_40}
    return path[correct]()
def f6_18():
    guess = myBitSolver.guess("001101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_41,3:f6_42,5:f6_43}
    return path[correct]()
def f6_19():
    return "000011"
def f6_20():
    guess = myBitSolver.guess("001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_44,5:f6_45}
    return path[correct]()
def f6_21():
    guess = myBitSolver.guess("000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f6_46,6:f6_47}
    return path[correct]()
def f6_22():
    return "111110"
def f6_23():
    return "111101"
def f6_24():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_48,2:f6_49}
    return path[correct]()
def f6_25():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_50,2:f6_51}
    return path[correct]()
def f6_26():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_52,3:f6_53}
    return path[correct]()
def f6_27():
    guess = myBitSolver.guess("000110")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_54,2:f6_55,4:f6_56}
    return path[correct]()
def f6_28():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_57,3:f6_58}
    return path[correct]()
def f6_29():
    return "110011"
def f6_30():
    guess = myBitSolver.guess("010100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_59,2:f6_60,4:f6_61}
    return path[correct]()
def f6_31():
    return "001111"
def f6_32():
    return "110100"
def f6_33():
    guess = myBitSolver.guess("001101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f6_62,2:f6_63,4:f6_64}
    return path[correct]()
def f6_34():
    guess = myBitSolver.guess("010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_65,3:f6_66,5:f6_67}
    return path[correct]()
def f6_35():
    guess = myBitSolver.guess("010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_68,3:f6_69,5:f6_70}
    return path[correct]()
def f6_36():
    guess = myBitSolver.guess("001101")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_71,4:f6_72,6:f6_73}
    return path[correct]()
def f6_37():
    return "001011"
def f6_38():
    return "110000"
def f6_39():
    guess = myBitSolver.guess("010100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_74,4:f6_75,6:f6_76}
    return path[correct]()
def f6_40():
    return "001100"
def f6_41():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_77,5:f6_78}
    return path[correct]()
def f6_42():
    guess = myBitSolver.guess("000110")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_79,4:f6_80,6:f6_81}
    return path[correct]()
def f6_43():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_82,5:f6_83}
    return path[correct]()
def f6_44():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f6_84,6:f6_85}
    return path[correct]()
def f6_45():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f6_86,6:f6_87}
    return path[correct]()
def f6_46():
    return "000010"
def f6_47():
    return "000001"
def f6_48():
    return "111011"
def f6_49():
    return "110111"
def f6_50():
    return "101111"
def f6_51():
    return "011111"
def f6_52():
    return "111010"
def f6_53():
    return "110110"
def f6_54():
    return "111001"
def f6_55():
    return "110101"
def f6_56():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_88,3:f6_89}
    return path[correct]()
def f6_57():
    return "101101"
def f6_58():
    return "011101"
def f6_59():
    return "101011"
def f6_60():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f6_90,3:f6_91}
    return path[correct]()
def f6_61():
    return "010111"
def f6_62():
    return "110010"
def f6_63():
    return "110001"
def f6_64():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_92,4:f6_93}
    return path[correct]()
def f6_65():
    return "101010"
def f6_66():
    guess = myBitSolver.guess("000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_94,4:f6_95}
    return path[correct]()
def f6_67():
    return "011001"
def f6_68():
    return "100110"
def f6_69():
    guess = myBitSolver.guess("000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_96,4:f6_97}
    return path[correct]()
def f6_70():
    return "010101"
def f6_71():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f6_98,4:f6_99}
    return path[correct]()
def f6_72():
    return "001110"
def f6_73():
    return "001101"
def f6_74():
    return "101000"
def f6_75():
    guess = myBitSolver.guess("000100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_100,5:f6_101}
    return path[correct]()
def f6_76():
    return "010100"
def f6_77():
    return "100010"
def f6_78():
    return "010010"
def f6_79():
    guess = myBitSolver.guess("010000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f6_102,5:f6_103}
    return path[correct]()
def f6_80():
    return "001010"
def f6_81():
    return "000110"
def f6_82():
    return "001001"
def f6_83():
    return "000101"
def f6_84():
    return "100000"
def f6_85():
    return "010000"
def f6_86():
    return "001000"
def f6_87():
    return "000100"
def f6_88():
    return "101110"
def f6_89():
    return "011110"
def f6_90():
    return "011011"
def f6_91():
    return "100111"
def f6_92():
    return "101100"
def f6_93():
    return "011100"
def f6_94():
    return "011010"
def f6_95():
    return "101001"
def f6_96():
    return "010110"
def f6_97():
    return "100101"
def f6_98():
    return "100011"
def f6_99():
    return "010011"
def f6_100():
    return "011000"
def f6_101():
    return "100100"
def f6_102():
    return "100001"
def f6_103():
    return "010001"

def f7_0():
    guess = myBitSolver.guess("0000000")
    myBitSolver.secOnes = round((7 + myBitSolver.allOnes - guess) / 2)
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_1,1:f7_2,2:f7_3,3:f7_4,4:f7_5,5:f7_6,6:f7_7,7:f7_8}
    return path[correct]()
def f7_1():
    return "1111111"
def f7_2():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_9,4:f7_10}
    return path[correct]()
def f7_3():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_11,3:f7_12,5:f7_13}
    return path[correct]()
def f7_4():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_14,2:f7_15,4:f7_16,6:f7_17}
    return path[correct]()
def f7_5():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_18,3:f7_19,5:f7_20,7:f7_21}
    return path[correct]()
def f7_6():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_22,4:f7_23,6:f7_24}
    return path[correct]()
def f7_7():
    guess = myBitSolver.guess("0000111")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_25,5:f7_26}
    return path[correct]()
def f7_8():
    return "0000000"
def f7_9():
    guess = myBitSolver.guess("0000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_27,2:f7_28}
    return path[correct]()
def f7_10():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_29,3:f7_30}
    return path[correct]()
def f7_11():
    guess = myBitSolver.guess("0000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_31,3:f7_32}
    return path[correct]()
def f7_12():
    guess = myBitSolver.guess("0001001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_33,2:f7_34,4:f7_35}
    return path[correct]()
def f7_13():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_36,2:f7_37,4:f7_38}
    return path[correct]()
def f7_14():
    return "1111000"
def f7_15():
    guess = myBitSolver.guess("0001011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_39,2:f7_40,4:f7_41}
    return path[correct]()
def f7_16():
    guess = myBitSolver.guess("0011001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_42,2:f7_43,4:f7_44,6:f7_45}
    return path[correct]()
def f7_17():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_46,3:f7_47}
    return path[correct]()
def f7_18():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_48,6:f7_49}
    return path[correct]()
def f7_19():
    guess = myBitSolver.guess("0011001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_50,3:f7_51,5:f7_52,7:f7_53}
    return path[correct]()
def f7_20():
    guess = myBitSolver.guess("0001011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_54,5:f7_55,7:f7_56}
    return path[correct]()
def f7_21():
    return "0000111"
def f7_22():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_57,5:f7_58,7:f7_59}
    return path[correct]()
def f7_23():
    guess = myBitSolver.guess("0001001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_60,5:f7_61,7:f7_62}
    return path[correct]()
def f7_24():
    guess = myBitSolver.guess("0000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_63,6:f7_64}
    return path[correct]()
def f7_25():
    guess = myBitSolver.guess("0011000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_65,6:f7_66}
    return path[correct]()
def f7_26():
    guess = myBitSolver.guess("0000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {5:f7_67,7:f7_68}
    return path[correct]()
def f7_27():
    return "1111110"
def f7_28():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_69,2:f7_70}
    return path[correct]()
def f7_29():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_71,2:f7_72}
    return path[correct]()
def f7_30():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_73,2:f7_74}
    return path[correct]()
def f7_31():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_75,3:f7_76}
    return path[correct]()
def f7_32():
    return "1111001"
def f7_33():
    return "1110110"
def f7_34():
    guess = myBitSolver.guess("0010011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_77,3:f7_78,5:f7_79}
    return path[correct]()
def f7_35():
    guess = myBitSolver.guess("0010010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_80,2:f7_81,4:f7_82}
    return path[correct]()
def f7_36():
    return "1100111"
def f7_37():
    guess = myBitSolver.guess("0101000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_83,2:f7_84,4:f7_85}
    return path[correct]()
def f7_38():
    return "0011111"
def f7_39():
    return "1110100"
def f7_40():
    guess = myBitSolver.guess("0010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_86,3:f7_87,5:f7_88}
    return path[correct]()
def f7_41():
    guess = myBitSolver.guess("0010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_89,3:f7_90,5:f7_91}
    return path[correct]()
def f7_42():
    return "1100110"
def f7_43():
    guess = myBitSolver.guess("0001010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_92,3:f7_93,5:f7_94}
    return path[correct]()
def f7_44():
    guess = myBitSolver.guess("0101011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_95,3:f7_96,5:f7_97,7:f7_98}
    return path[correct]()
def f7_45():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_99,4:f7_100}
    return path[correct]()
def f7_46():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_101,4:f7_102}
    return path[correct]()
def f7_47():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_103,4:f7_104}
    return path[correct]()
def f7_48():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_105,5:f7_106}
    return path[correct]()
def f7_49():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_107,5:f7_108}
    return path[correct]()
def f7_50():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_109,5:f7_110}
    return path[correct]()
def f7_51():
    guess = myBitSolver.guess("0101010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_111,3:f7_112,5:f7_113,7:f7_114}
    return path[correct]()
def f7_52():
    guess = myBitSolver.guess("0001010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_115,4:f7_116,6:f7_117}
    return path[correct]()
def f7_53():
    return "0011001"
def f7_54():
    guess = myBitSolver.guess("0010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_118,4:f7_119,6:f7_120}
    return path[correct]()
def f7_55():
    guess = myBitSolver.guess("0010001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_121,4:f7_122,6:f7_123}
    return path[correct]()
def f7_56():
    return "0001011"
def f7_57():
    return "1100000"
def f7_58():
    guess = myBitSolver.guess("0101000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_124,5:f7_125,7:f7_126}
    return path[correct]()
def f7_59():
    return "0011000"
def f7_60():
    guess = myBitSolver.guess("0010010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_127,5:f7_128,7:f7_129}
    return path[correct]()
def f7_61():
    guess = myBitSolver.guess("0010011")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_130,4:f7_131,6:f7_132}
    return path[correct]()
def f7_62():
    return "0001001"
def f7_63():
    return "0000110"
def f7_64():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_133,6:f7_134}
    return path[correct]()
def f7_65():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {5:f7_135,7:f7_136}
    return path[correct]()
def f7_66():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {5:f7_137,7:f7_138}
    return path[correct]()
def f7_67():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {5:f7_139,7:f7_140}
    return path[correct]()
def f7_68():
    return "0000001"
def f7_69():
    return "1111101"
def f7_70():
    return "1111011"
def f7_71():
    return "1110111"
def f7_72():
    return "1101111"
def f7_73():
    return "1011111"
def f7_74():
    return "0111111"
def f7_75():
    return "1111100"
def f7_76():
    return "1111010"
def f7_77():
    return "1101110"
def f7_78():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_141,2:f7_142,4:f7_143}
    return path[correct]()
def f7_79():
    return "1110011"
def f7_80():
    return "1101101"
def f7_81():
    guess = myBitSolver.guess("0100010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {0:f7_144,2:f7_145,4:f7_146}
    return path[correct]()
def f7_82():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_147,3:f7_148}
    return path[correct]()
def f7_83():
    return "1010111"
def f7_84():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_149,3:f7_150}
    return path[correct]()
def f7_85():
    return "0101111"
def f7_86():
    return "1101100"
def f7_87():
    guess = myBitSolver.guess("0100010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_151,3:f7_152,5:f7_153}
    return path[correct]()
def f7_88():
    return "1110001"
def f7_89():
    return "1101010"
def f7_90():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_154,3:f7_155,5:f7_156}
    return path[correct]()
def f7_91():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_157,4:f7_158}
    return path[correct]()
def f7_92():
    return "1100101"
def f7_93():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_159,3:f7_160,5:f7_161}
    return path[correct]()
def f7_94():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_162,4:f7_163}
    return path[correct]()
def f7_95():
    return "1010101"
def f7_96():
    guess = myBitSolver.guess("0001010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_164,3:f7_165,5:f7_166}
    return path[correct]()
def f7_97():
    guess = myBitSolver.guess("0001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {1:f7_167,3:f7_168,5:f7_169}
    return path[correct]()
def f7_98():
    return "0101011"
def f7_99():
    return "0011101"
def f7_100():
    return "0011011"
def f7_101():
    return "1000111"
def f7_102():
    return "0100111"
def f7_103():
    return "0010111"
def f7_104():
    return "0001111"
def f7_105():
    return "1110000"
def f7_106():
    return "1101000"
def f7_107():
    return "1011000"
def f7_108():
    return "0111000"
def f7_109():
    return "1100100"
def f7_110():
    return "1100010"
def f7_111():
    return "1010100"
def f7_112():
    guess = myBitSolver.guess("0001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_170,4:f7_171,6:f7_172}
    return path[correct]()
def f7_113():
    guess = myBitSolver.guess("0001100")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_173,4:f7_174,6:f7_175}
    return path[correct]()
def f7_114():
    return "0101010"
def f7_115():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_176,5:f7_177}
    return path[correct]()
def f7_116():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_178,4:f7_179,6:f7_180}
    return path[correct]()
def f7_117():
    return "0011010"
def f7_118():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_181,5:f7_182}
    return path[correct]()
def f7_119():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_183,4:f7_184,6:f7_185}
    return path[correct]()
def f7_120():
    return "0010101"
def f7_121():
    return "0001110"
def f7_122():
    guess = myBitSolver.guess("0100010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_186,4:f7_187,6:f7_188}
    return path[correct]()
def f7_123():
    return "0010011"
def f7_124():
    return "1010000"
def f7_125():
    guess = myBitSolver.guess("0001000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_189,6:f7_190}
    return path[correct]()
def f7_126():
    return "0101000"
def f7_127():
    guess = myBitSolver.guess("0100000")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {4:f7_191,6:f7_192}
    return path[correct]()
def f7_128():
    guess = myBitSolver.guess("0100010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_193,5:f7_194,7:f7_195}
    return path[correct]()
def f7_129():
    return "0010010"
def f7_130():
    return "0001100"
def f7_131():
    guess = myBitSolver.guess("0100001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_196,5:f7_197,7:f7_198}
    return path[correct]()
def f7_132():
    return "0010001"
def f7_133():
    return "0000101"
def f7_134():
    return "0000011"
def f7_135():
    return "1000000"
def f7_136():
    return "0100000"
def f7_137():
    return "0010000"
def f7_138():
    return "0001000"
def f7_139():
    return "0000100"
def f7_140():
    return "0000010"
def f7_141():
    return "1011110"
def f7_142():
    return "0111110"
def f7_143():
    return "1110101"
def f7_144():
    return "1011101"
def f7_145():
    return "0111101"
def f7_146():
    return "1101011"
def f7_147():
    return "1011011"
def f7_148():
    return "0111011"
def f7_149():
    return "0110111"
def f7_150():
    return "1001111"
def f7_151():
    return "1011100"
def f7_152():
    return "0111100"
def f7_153():
    return "1110010"
def f7_154():
    return "1011010"
def f7_155():
    return "0111010"
def f7_156():
    return "1101001"
def f7_157():
    return "1011001"
def f7_158():
    return "0111001"
def f7_159():
    return "1010110"
def f7_160():
    return "0110110"
def f7_161():
    return "1100011"
def f7_162():
    return "1001110"
def f7_163():
    return "0101110"
def f7_164():
    return "0110101"
def f7_165():
    guess = myBitSolver.guess("0000010")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {2:f7_199,4:f7_200}
    return path[correct]()
def f7_166():
    return "0011110"
def f7_167():
    return "0110011"
def f7_168():
    return "1001011"
def f7_169():
    return "0101101"
def f7_170():
    guess = myBitSolver.guess("0000001")
    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)
    path = {3:f7_201,5:f7_202}
    return path[correct]()
def f7_171():
    return "0110100"
def f7_172():
    return "1001100"
def f7_173():
    return "0110010"
def f7_174():
    return "1001010"
def f7_175():
    return "0101100"
def f7_176():
    return "1010001"
def f7_177():
    return "0110001"
def f7_178():
    return "0011100"
def f7_179():
    return "1001001"
def f7_180():
    return "0101001"
def f7_181():
    return "1000110"
def f7_182():
    return "0100110"
def f7_183():
    return "0010110"
def f7_184():
    return "1000101"
def f7_185():
    return "0100101"
def f7_186():
    return "0001101"
def f7_187():
    return "1000011"
def f7_188():
    return "0100011"
def f7_189():
    return "0110000"
def f7_190():
    return "1001000"
def f7_191():
    return "1000100"
def f7_192():
    return "0100100"
def f7_193():
    return "0010100"
def f7_194():
    return "1000010"
def f7_195():
    return "0100010"
def f7_196():
    return "0001010"
def f7_197():
    return "1000001"
def f7_198():
    return "0100001"
def f7_199():
    return "1001101"
def f7_200():
    return "1010011"
def f7_201():
    return "1010010"
def f7_202():
    return "1100001"


class bits():
    # A class to handle generating 100 random bits and test guessing

    def __init__(self):
        # Build our string of 100 random bits
        self.string = ''
        for i in range(100):
            self.string += str(random.randint(0, 1))
        # Set our guesses at 0
        self.guesses = 0

    def guess(self, input):
        # Start with 0 correct
        count = 0
        # For each correct pair in our bits/input, increment count
        for i in range(len(self.string)):
            if self.string[i] == input[i]:
                count += 1
        # Increase guesses by 1 and return count
        self.guesses += 1
        return count


class bitSolver():
    # A class that handle how to guess to solve the bits

    def __init__(self, bitInstance_, size):
        # Start of with none of the bits known
        self.pos = 0
        # Specify the size of the chunking we're doing
        self.size = size
        # Get a reference to the bits we're trying to solve
        self.bitInstance = bitInstance_
        # Store a list of our known bits
        self.knownBits = ""
        # Take our first guess as all 1's
        newGuess = '1' * 100
        self.allOnes = self.bitInstance.guess(newGuess)

    def guess(self, input):
        # Take a guess. The guess is all 1's except for the input, which is placed at self.pos location in the guess

        # Create the first part of the guess
        newGuess = '1' * self.pos
        # Add the input as the middle section of the guess
        newGuess += input
        # Finish off the guess
        while len(newGuess) < 100:
            newGuess += "1"
        # Take the guess and return the number of correct positions
        retrunVal = self.bitInstance.guess(newGuess)
        return retrunVal

    def update(self):
        # Call the respective function depending on the size of our chunking
        # This function will make a series of guesses and return the correct series of bits
        if self.size == 1:
            self.knownBits += f1_0()
        elif self.size == 2:
            self.knownBits += f2_0()
        elif self.size == 3:
            self.knownBits += f3_0()
        elif self.size == 4:
            self.knownBits += f4_0()
        elif self.size == 5:
            self.knownBits += f5_0()
        elif self.size == 6:
            self.knownBits += f6_0()
        elif self.size == 7:
            self.knownBits += f7_0()

        # Move our position up
        self.pos += self.size


# Specify the size of our chunking
size = 5

# We're calculating an average number of guesses. Store the total guesses in averageCounter
averageCounter = 0
# Specify how many tests to run
maxTest = 1000

# Store how many chunking guesses we should take given the size of chunking
maxCounter = math.floor(100 / size)
for test in range(maxTest):
    print(test)
    # Create a new random bitstring
    myBits = bits()
    # Create a new bitSolver
    myBitSolver = bitSolver(myBits, size)

    # Use the chunkng approach as many times as we can (eg, if chunking is 7, we can only use it for first 98 bits
    for i in range(maxCounter):
        myBitSolver.update()

    # If there's a few bits remaining, change our size of chunking to that remainder and apply 1 more chunk
    if (maxCounter * size != 100):
        myBitSolver.size = 100 - maxCounter * size
        myBitSolver.update()

    # Our guess at the bits should match the actual bits by now
    assert myBitSolver.knownBits == myBits.string, "What the hell happened"

    # Incrament how many guesses it took
    averageCounter += myBits.guesses
# Print the average of how many guesses it took
print(averageCounter / maxTest)
