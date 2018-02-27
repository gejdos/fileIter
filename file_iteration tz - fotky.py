import os
import shutil

directory_in_str1 = r"C:\Users\Jakub\Desktop\galeriatz"
directory_in_str2 = r"C:\Users\Jakub\Desktop\Janko foto"
directory1 = os.fsencode(directory_in_str1)
directory2 = os.fsencode(directory_in_str2)
target=r"C:\Users\Jakub\Desktop\final"

i=0
for f1 in os.listdir(directory1):
    fname1 = os.fsdecode(f1)
    for f2 in os.listdir(directory2):
        fname2 = os.fsdecode(f2)
        if fname1==fname2:
            dir1 = os.fsencode(directory_in_str1 + "\\" + fname1)
            dir2 = os.fsencode(directory_in_str2 + "\\" + fname2)
            for g1 in os.listdir(dir1):
                gname1 = os.fsdecode(g1)
                for g2 in os.listdir(dir2):
                    gname2 = os.fsdecode(g2)
                    if gname1==gname2:
                        if not os.path.exists(target + "\\" + fname1):
                            os.mkdir(target + "\\" + fname1)
                        shutil.copy(directory_in_str2 + "\\" + fname2 + "\\" + gname2, target + "\\" + fname1)
    i+=1
    print("Zlozka c. " + str(i))
