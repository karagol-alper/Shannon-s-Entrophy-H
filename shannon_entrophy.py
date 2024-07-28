# -*- coding: utf-8 -*-
"""Shannon entrophy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e-PNaWoSZ1mmWraCcAPyu8S9lBFBQlXY

## Shannon entrophy (H) calculation
"""

import numpy as np

def calculate_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    probabilities = [count / len(sequence) for count in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probabilities)
    return entropy

# Simply replace below with your sequance, you can add more sequences.
cs = "GAAAAAGGAACTTTCTCGTAACAGTTGTACAACCAGGCTAAAGAGCACACCCTCGCCTTCCCTGAAGGGGAGGAAACATGCAATAATGTGAGGTAATTAAATTTAGCCTTAGAAAAGTCTTTGAAAAGTTCTAATCAAGACTTTCAGCTTTCCGATTGTGTGCGCTTTATTTTTCAATTCTTCCTAGTCCCGGTTTTGCATTTCTAATGACAGTGAACTGACAAAGCGTGAAAGTGGTCTAAGGAGCAAAACAAAGCCAGCAAGCCTGCTTCTGGTGTGCCAAGATTAATCAATATTCCAGAAACCTCGGGGTTTCCCCCTCCTCCCCTGTGCGGTTTCCATTCCCCACTCCTCCTTTCCCGGGCACAGACTCCTCCCCTTTTCTTAAGTTGCCCTGATAGTAACTTGCAGTTTCAGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCGTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAGGCAAACTGTTAAGTCTTTTTTTTTCCTGCACTGGGATTGCAAGAAGTCATTTGCGAGGAGTCCTTTGGTTTCCAGTTACCTCCCCCACAGGCGCACACGCTGGCTGCTTGCGTTGGCAGCGACACACATCCATGCTGTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGACCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACAGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCGCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACAAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTGTGGGTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTTACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCCATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTGACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACCGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTAAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCTGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATAAAGAAACACTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAGTCCTCCAAAACACAAGGGAGGATTTTGGGTGGCCAAAGTGTACAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTTTATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCGGTTATCAGTTGGACAGTAAGATTTTATCCCTTTCTCTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGACAGACAGAAGGCAAAGTTTCCATGTGGCCTTGAGCAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGAAGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCTGCCCTCTGTTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATCAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGATGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATAAAAAAGAAGAGGTTCATTTTTCTGGCTTTCTTTTTTTCACCTGAAACACTTTTTTCTCTTGAGTCCAAAATCATTCCCCCCATGAAGTCTGCTTACCAAAACATAAGACGACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCATGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAATGAGGGAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCATAAGAGAAATGGTAGAAGATGAATCAGTATGAAGACACTGTCAATGAGGTTATGAGAAAAAAACAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAAACTGAAAAATCTAGACATAGATCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCTGTGGTGCAGTAACCATTTAATGTCGAGGCTCTATTTCGGAAATACACTACAAATGTTAAAGTACGTGGCTGTCCTCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATATGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGCACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAAAGATAGTTTTACATTAA"
s1 = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------GCTTTATTTTTCAATTCTTCCTAGTCCCGGTTTTGCATTTCTAATGACAGTGAACTGACAAAGCGTGAAAGTGGTCTAAGGAGCAAAACAAAGCCAGCAAGCCTGCTTCTGGTGTGCCAAGATTAATCAATATTCCAGAAACCTCGGGGTTTCCCCCTCCTCCC-TGTGCGGTTTCCATTCCCCACTCCTCCTTTCCCGGGCACAGACTCCTCCCCTTTTCTTAAGTTGCCCTGATAGTAACTTGCAGTTTCAGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCGTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAG----------------------------------------------T----------------------------------------------------------------------------------------TGTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGACCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACAGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCGCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACAAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTTTGGTTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTTACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCCATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCTCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTCACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACCGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTTGTGCTTCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTTAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCTGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATAAAGAAACACTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAGTCCTCCAAAACACAAGGGAGGATTTTGGGTGGCCAAAGTGTACAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTT-ATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCGGTTATCAGTTGGACAGCAAGATTTTATCCCTTTCTGTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGACAGACAGAAGGCAAAGTTTCCATGTGGCCTTGAGTAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGAAGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCTGCCCTCTGTTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATCAAACTCTTTGTCCAGTTCATCCGAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCAAAAACAGATGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCCAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATAAAAAAGAAGAGGTTCATTTTTCTGGCTTT--TTTTTTCACCTGAAACACTTTTT-CTC--GAGTCCAAAATCATTCCCCC-ATGAAGTCTGCTTACCAAAACATAAGATGACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCATGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAACCAAAAGTCCTTAGAATGAGGGAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCATAAGAGAAATGGTAGAAGATGAATCAGTATGAAGAAACTGTCAATGAGGTTATGAGAAAAAA-CAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGGGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGATTTAATTATGCTAACAAACTGAAAAATCTAGACATAGGTCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCTGTGGTGCAGTAACCATTTAATGTCGAGGCTCTATTTCGGAAATACACTACAAATGTTAAAGTACGTGACTGTCCTCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATATGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGTACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAAA-ATAGTTTTACATTAA"
s2 = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------AGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCGTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAG----------------------------------------------T----------------------------------------------------------------------------------------TGTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGACCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACAGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCGCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACGAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTGTGGGTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTTACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCCATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTGACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCTTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACCGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTTAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCTGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATAAAGAAACACTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTCATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAATAGTCCTCCAAAACACAAGGGAGGATTTTGGGTGGCCAAAGTGTACAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCGAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTTTATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCGGTTATCAGTTGGACAGTAAGATTTTATCCCTTTCTCTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGACAGACAGAAGGCAAAGTTTCCATGTGGCCTTGAGCAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGAAGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCTGCCCTCTGTTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATCAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGATGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATAAAAAAGAAGAGGTTCATTTTTCTGGCTTT--TTTTTTCACCTGAAACACTTTTT-CTC--GAGTCCAAAATCATTCCCCCCGTGAAGTCTGCTTACCAAAACATAAGACGACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCATGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAATGAGGGAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCATAAGAGAAATGGTAGAAGATGAATCAGTATGAAGACACTGTCAATGAGGTTATGAGAAAAAAACAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAAACTGAAAAATCTAGACATAGATCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGCATAAAAGTTAACATTAGGCTGTGGTGCAGTAACCATTTAATGTCGAGGCTCTATTTCGGAAATACACTACAAATGTTAAAGTACGTGGCTGTCCTCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATATGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGCACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAAA-ATAGTTTTACATTAA"
s3 = "--AAAAGGAACTTTTTCGTAACAGTTGTACAACCAGGCTAAAGAGCACACCCTCGCCTTCCCTGAAGGGGAGGAAACCTGCAATAATGTGAGGTAATTAAATTTAGCCTTAGAAAAGTCTTTGAAAAGTTCTAATCAAGACTTTCAGCTTTCCGATTGTGTGCGCTTTATTTTTCAATTCTTCCTAGTCCCGGTTTTGCATTTCTAATGACAGTGAACTGACAAAGCGTGAAAGTGGTCTAAGGAGCAAAACAAAGCCAGCAAGCCTGCTTCTGGTGTGCCAAGATTAATCAATATTCCAGAAACCTCGGGGTTTCCCCCTCCTCCCCTGTGCGGTTTCCATTCCCCACTCCTCCTTTCCCGGGCACAGACTCCTCCCCTTTTCTTAAGTTGCCCTGATAGTAACTTGCAGTTTCAGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCCTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAGGCAAACTGTTAAGTCTTTTTTTTTCCTGCACTGGGATTGCAAGAAGTCATTTGCGAGGAGTCCTTTGGTTTCCAGTTACCTCCCCCACAGGCGCACACGCTGGCTGCTTGCGTTGGCAGCGACACACATCCCTGCTGTGGTTTCTAACACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGACCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACTGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCCCTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCTCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAGTTGTACGAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCGAATCTGGTAGAAGCTTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTGTGGGTGCTGTGATAAACAACGTGTCTGAGGCCATGGAGACTCTTACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCCATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAATGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGCGTGATTGGGGGGCAGCTTGCCATGTACACTGTGACTGTCATTGTTGGCTTACTCATTCACGCAGCCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTTATCACTGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTAAACAACTTTGAACTGAACTTCGGACAGATTATTACAATCAGCATCACAGCCACGGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCCGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCTTATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCGTCGACAGTGAAACCAAGATGTAGACTAACATAAAGAAACGCTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCGTTACAGCTCATTCTCTCCAGCAAGCCCCTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAGTCCTCCAAAAAACAAGGGAGGATTTTGGGTGGCCAAAGTATATAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCAAAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTT-ATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTGAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCGGTTATCAGTTGGACAGTAAGATTTTGTCCCTTTCTCTTCTGACCGGTATACCTATTTCATTAGTAGCTAGGTGCACGTATACATCTAGCACAGCTGTGAGGAGAGACAGAAG-CAAAGTTTCCATGTGGCCTTGAGTAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGATGTCTTCGTGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCCGCCCTCTACTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTGTAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCATGAGTGGGATTATTCATAAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTACTCCCTTCTTTCCTGCTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGAAGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGACTTGAGCACAGGCAACATTATAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATAAAAAAGAAGAGGTTCATTTTTCTGGCTTT--TTTTTTCACCTGAAACACTTTTT-CTCTTGAGTCCAAAATCACTCCCCC-ATGAAGTCTGCCTACCAAAACGTAAGACCACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCGTGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAACGAGAGAAACAAAATATTTATTTGTTTTGGAATCCCACTTAACAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCGTAAGAGAAATGGTAGAAGACGAATCAGTACGAAGACACTGTCAATGAGGTTATGAGAAAAAA-CAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAGACTGAAAA-TCTAGACATACATCCTCTGATATACAATTAGAGATATTTTTGTATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCTGTGGTGGAGTAACCATTTAATGTCGTGGCTCTATTTGGGAAATACACTACAAACGTTAAAGTACGTGGCTGTCATCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATGTGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGCACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAAAGATAGTTTTACATTAA"
s4 = "GAAAAAGGAACTTTCTCGTAACAGTTGTACAACCAGGCTAAAGAGCACACCCTCGTCTTCCCTGAAGGGGAGGAAACATGCAATAATGTGAGGTAATTAAATTTAGCCTTAGAAAAGTCTTTGAAACGTTCTAATCAAGACTTTCAGCTTTCCGATTGTGTGCGCTTTATTTTTCAATTCTTCCTAGTCCCGGTTTTGCATTTCTAATGACAGTGAACTGACAAAGCGTGAAAGTGGTCTAAGGAGCAAAACAAAGCCAGCAAGCCTGCTTCTGGTGTGCCAAGATTAATCAATATTCCAGAAACCTCGGGGTTTCCCC-TCCTCCC-TGTGCGGTTTCCATTCCCCACTCCTCCTTTCCCGGGCACAGACTCCTCCCCTTTTCTTAAGTTGCCCTGATAGTAACTTGCAGTTTCAGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCGTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAG----------------------------------------------TCATTTGCGAGGAGTCCTTTGGTTTCCAGTTACCTCCCCCACAGGCGCACACGCTGGCTGCTTGCGTTGGCAGCGATACACATCCATGTTCTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGGCCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACAGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCGCTAGATAGTAAGGCATCGGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACAAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTGTGGGTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTCACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCTATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTGACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACCGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTAAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCTGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATGAAGAAACACTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAGTCCTCCAAAACACAAGGGAGGATTTTGGGTGGCCAAAGTGTACAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTT-ATATAAGTTAAAGAGACAAATAGTAGGCTACAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCAGTTATCAGTTGGACAGTAAGATTTTATCCCTTTCTCTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGACAGACAGAAGGCAAAGTTTCCATGTGGCCTTGAGCAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGAAGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCTGCCCTCTGTTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTAGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATCAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGATGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATAACAAAGAAGAGGTTCATTTTTCTGGCTTTCTTTTTTTCACCTGAAACACTTTTT-CTC--GAGTCCAAAATCATGCCCCC-GTGAAGTCTGCTTACCAAAACATAAGACGACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCATGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAATGAGGGAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCATAAGAGAAATGGTAGAAGATGAATCAGTATGAAGACACTGTCAATGAGGTTATGAGAAAAAA-CAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAAACTGAAAAATCTAGACATAGATCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCCGTGGTGCAGTAACCATTTAATGTCGAGGCTCTATTTTGGAAATACACTACAAATGTTAAAGTACGTGGCTGTCCTCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATATGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGCACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAAA-TTAGTTTTACATTAA"
s5 = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------GCTTTATTTTTCAATTCTTCCTAGTCCCGGTTTTGCATTTCTAATGACAGTGAACTGACAAAGCGTGAAAGTGGTCTAAGGAGCAAAACAAAGCCAGCAAGCCTGCTTCTGGTGTGCCAAGATTAATCAATATTCCAGAAACCTCGGGGTTTCCCC-TCCTCCC-TGTGCGGTTTCCATTCCCCACTCCTCCTTTCCCGGGCACAGACTCCTCCCCTTTTCTTAAGTTGCCCTGATAGTAACTTGCAGTTTCAGAGCACATGCACACTGTCAGGGCTAGCCTGCCTGCTTACGCGCGCTGCGGATTGTTGCTCCGTTGTACCTGCTGGGGAATTCACCTCGTTACTGCTTGATATCTTCCACCCCTTACAAAATCAGAAAAG----------------------------------------------T----------------------------------------------------------------------------------------TCTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGGCCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGGGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACAGTCACCGCTGTCATTGTTGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCGGCGCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACAAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTTGTGGGTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTCACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCTATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTGACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACCGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCCGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTAAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGTATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCGGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGGGCTGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGTTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATGAAGAAACACTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAGTCCTCCAAAACACAAGGGAGGATTTTGGGTGGCCAAAGTGTACAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTT-ATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGAAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCAGTTATCAGTTGGACAGTAAGATTTTATCCCTTTCTCTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGACAGACAGAGGGCAAAGTTTCCATGTGGCCTTGAGCAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGAAGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCACCTGCCCTCTGTTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGAGGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATCAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTTTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGATGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGTCTTCTTTAAGGAAGAATACAAAAGAAGAGGTTCATTTTTCTGGCTTT-TTTTTTTCACCTGAAACACTTTTT-CTC--GAGTCCAAAATCATTCCCCC-GTGAAGTCTGCTTACCAAAACATAAGACGACTTATATATTTGAAAGAAGTCAAATGAATGAGCTCTCTAATAGAAGTCCATGAGTTGAGTGGGTATTTCTTATTTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAATGAGGGAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATCATTCAAAACTTTCAGCTGGAGTGGGGTTTGTTTTTGTTTTGTTTGTGTCCATAAGAGAAATGGTAGAAGATGAATCAGTATGAAGACACTGTCAATGAGGTTATGAGAAAAAA-CAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTACCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAAACTGAAAAATCTAGACATAGATCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCCGTGGTGCAGTAACCATTTAATGTCGAGGCTCTATTTTGGAAATACACTACAAATGTTAAAGTACGTGGCTGTCCTCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATATGTGTTTTTTAATATACTAACCATTTCTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATACACATGCACTCAGTGTGGACTGGGAAGCATTACTTTGTAGATGTATTTTCAATAAAGAAAAA--TTAGTTTTACATTAA"
s6 = "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------GAAAGAAAAACTGGGGGGAAAAAGATCTCTGAATCCTTTGGGATTTAATGGAGGA---AAGGTGCAAGTCCAAGCAGCTCTCTAGAAAGAGGA-GACTCCAGCTACCCTGTGCAGGGCTTGAAGGT---------------------------------------------------------------------------------------------------------------------------------------TGTGTTTTCTAATACCAAAGAGGAGGTTTGGCTTTCTGTGGGTGATTCCCAGACACTGAAGTGCAAAGAAGAGACCCTCCTAGAAAAGTAAAATATGACTAAAAGCAATGGAGAAGAGCCCAAGATGGGCGGCAGGATGGAGAGATTCCAGCAGGGAGTCCGTAAACGCACACTTTTGGCCAAGAAGAAAGTGCAGAACATTACAAAGGAGGATGTTAAAAGTTACCTGTTTCGGAATGCTTTTGTGCTGCTCACTGTCACCGCTGTCATTGTGGGTACAATCCTTGGATTTACCCTCCGACCATACAGAATGAGCTACCGGGAAGTCAAGTACTTCTCCTTTCCTGGGGAACTTCTGATGAGGATGTTACAGATGCTGGTCTTACCACTTATCATCTCCAGTCTTGTCACAGGAATGGCAGCGCTAGATAGTAAGGCATCAGGGAAGATGGGAATGCGAGCTGTAGTCTATTATATGACTACCACCATCATTGCTGTGGTGATTGGCATAATCATTGTCATCATCATCCATCCTGGGAAGGGCACAAAGGAAAACATGCACAGAGAAGGCAAAATTGTACAAGTGACAGCTGCAGATGCCTTCCTGGACTTGATCAGGAACATGTTCCCTCCAAATCTGGTAGAAGCCTGCTTTAAACAGTTTAAAACCAACTATGAGAAGAGAAGCTTTAAAGTGCCCATCCAGGCCAACGAAACGCTCGTGGGTGCTGTGATAAACAATGTGTCTGAGGCCATGGAGACTCTTACCCGAATCACAGAGGAGCTGGTCCCAGTTCCAGGATCTGTGAATGGAGTCAATGCCCTGGGTCTAGTTGTCTTCTCCATGTGCTTCGGTTTTGTGATTGGAAACATGAAGGAACAGGGGCAGGCCCTGAGAGAGTTCTTTGATTCTCTTAACGAAGCCATCATGAGACTGGTAGCAGTAATAATGTGGTATGCCCCCGTGGGTATTCTCTTCCTGATTGCTGGGAAGATTGTGGAGATGGAAGACATGGGTGTGATTGGGGGGCAGCTTGCCATGTACACCGTGACTGTCATTGTTGGCTTACTCATTCACGCAGTCATCGTCCTGCCACTCCTCTACTTCTTGGTAACACGGAAAAACCCTTGGGTTTTTATTGGAGGGTTGCTGCAAGCACTCATCACTGCTCTGGGGACCTCTTCAAGTTCTGCCACCCTACCCATCACCTTCAAGTGCCTGGAAGAGAACAATGGCGTGGACAAGCGCGTCACCAGATTCGTGCTCCCTGTAGGAGCCACCATTAACATGGATGGGACTGCCCTCTATGAGGCTTTGGCTGCCATTTTCATTGCTCAAGTTAACAACTTTGAACTGAACTTCGGACAAATTATTACAATCAGCATCACAGCCACAGCTGCCAGCATTGGGGCAGCTGGAATTCCTCAGGCGGGCCTGGTCACTATGGTCATTGTGCTGACATCTGTCGGCCTGCCCACTGACGACATCACGCTCATCATCGCAGTGGACTGGTTCCTGGATCGCCTCCGGACCACCACCAACGTACTGGGAGACTCCCTGGGAGCCGGGATTGTGGAGCACTTGTCACGACATGAACTGAAGAACAGAGATGCTGAAATGGGTAACTCAGTGATTGAAGAGAATGAAATGAAGAAACCATATCAACTGATTGCACAGGACAATGAAACTGAGAAACCCATCGACAGTGAAACCAAGATGTAGACTAACATAAAGAAATGCTTTCTTGAGCACCAGGTGTTAAAAACCATTATAAAATCTTTCCATCTCATTACAGCTCATTCGCTCCAGCAAGCCCGTTATCTTCCCTTTCCTCCCTTCTGATAAGACTGGAAAGTAATCCTCCAAAAAACAAGGGAGGATTTTGGGTGGCCAAAGTGTATAATTTTCATCCCACAATTGAAATTTTTAAATCATTTCATGTTAGTCTTACCTAATAAGGTACCAAGATCACAAATAGTGTTGATCAGATCTTACAAGTTTATGTGGCACACAATCCTATAAATGTGATTTTTT-ATATAAGTTAAAGAGACAAATAGTAGGCTAAAAACATTTTAAAATCAACTTTTGTAATTTAAAAATCTTTCAGAATACAATTCAGTTTTAGTTTCAAAATGTTAACAACTTGAATTACAACCGGTTATCAGTTGGACAGTAAGATTTTGTCCCTTTCTCTTCTGACTGGTATACCTATTTCATTAGTAGCTAGGTGCACATATACATCTAGCACAGCTGTGAGGAGAGACAGAAGGCAAAGTTTCCATGTAGCCTTGAGTAAGTCCCATCTCACCTCTAGGCCTCAGTGTCCTCATCTATAAAATGAGGGACTTCCCTAGATGTCTTCATGGTCTCTTCCAGCCCAGACATCCTGTGATGTCATGAAAGCAGCTGCCCTCTATTTCCCCTCAGAACACCCTGTACCATCCATGGAGCACGATGCCTTCAGAAAAGACACTTCAATGGGAGTGAACATTTCTAACTAAGGACAGGATGGCTGTGTGTGGTGGTCACCAGGTCCTGTGAGCAAAGTGCAGGTTATGCAAGTCGCCAGGCAGGAGGCCATTCCAGGAGTGGGATTATTCATAAAACTCTTTGCCCAGTTCATCCCAATGGGGGAAGTATTCCCTTCTTTCCTACTCTGGGAAGAATGTCTCCTGCCACTCCTCAACTGATGATAGACTTCGAAAACAGAAGAGAAGACTAGCAGCTAGCAAGGGTGCTTGTGGTCACACTGTGGAACACTAAAGAGCTAGGAAAGAGTTGAGCACAGGCAACATTACAAACAAAGGATTTGAAAACACCAAGAGTACAGGACTTCTTTAAGGAAGAATAAAAAAGAAGAGGTTCATTTTTCTGGCTTT--TTTTTTCAACTGAAACACTTTTTTCTCTTGAGTCCAAAATCATTCCCCC-ATGAAGTCTGCCTACCAAAACATAAGACGACTTATATATTTGAAGGAAGTCAAATGAATGAGCTCTCTAACAGAAGTGCATGAGTTGAGTGGGTATTTCTTATCTGAAAGTGTTTTTCTTTAATCAAAAGTCCTTAGAATGAGGAAAACAAAATATTTATTTGTTTTGGAATCCCACTTATCAAATAATTCAAAACTTTCAGCTGGAGTGGGGTTTGCTTTTGTTTTGTTTGTGTCCATAAGACAAATGGTAGAAGATGAATCAGTATGAAGACACTGTCAATGAGGTTATGAGAAGAAA-CAGCAGGGGCATTAGTTTCAGGCAAGGCAGCTCCCAGGTTTAGAGATTAATTTTTATCCCCTAAGGAATATCCAGTCAAAGACGCTGAGTGGGAGCTGTCAGGCAGTAGCAGCTGTGTTTGAGTTTCTGGCTGAAAATGGTGAAGAATGGACTTAATTATGCTAACAGACTGAAAA-TCTAGACATACATCCTCTGATATACAATTAGAGATATTTTTATATAGACCCCAAGCATTCTGTGTATAAAAGTTAACATTAGGCTGTGGTGCAGTAACCATTTAATGTCGAAGCTCTATTTGGGAAATACACTACAAATGTTAAAGTACGTGGCTGTCATCTTAAGACACTAGTAGAGCAAAGACTTAATCATATCAACTTAATTCTGTTACACAATGTATGTTTTTTAATATACTAACCATTTTTTATGGAAAGGTCCTGTGGGGAGCCCATCCTCTCGCCAAGCCATCACAGGCTCTGCATATACATGCACTCAGTGTGGACTGGGAAGCACTACTTTGTAGATGTATTTTCAATAAAGAAAAAA-ATAGTTTT-------"

sequences = [cs,s1,s2,s3,s4,s5,s6]  # replace with your sequences names
entropies = [calculate_entropy(seq) for seq in sequences]
print(entropies)