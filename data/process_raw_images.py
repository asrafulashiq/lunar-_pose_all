#%%
from pathlib2 import Path
import cv2
from matplotlib import pyplot as plt
import random

FLDR = Path('./raw_images')
TRN_DEST = Path('./training')
TEST_DEST = Path('./testing')
print Path('.').absolute()

if not TRN_DEST.exists():
    TRN_DEST.mkdir()

if not TEST_DEST.exists():
    TEST_DEST.mkdir()

#%%
for vid_file in FLDR.iterdir():
    print "src: ", vid_file

    # if vid_file.name != '10_17_T4_K1':
    #     continue
    # else:
    #     print 'processing'

    allfiles = sorted(list(vid_file.iterdir()))
    num_sampled = 120
    train_sample = 100
    test_sample = 20
    shuffled_files = random.sample(allfiles, num_sampled)
    shuffled_train = shuffled_files[:train_sample]
    shuffled_test = shuffled_files[train_sample:]

    for imfile in shuffled_files:
        is_train = False
        if imfile in shuffled_train:
            is_train = True

        imfile = str(imfile)
        if not imfile.endswith('jpg'):
            continue
        im_s = cv2.imread(imfile, cv2.IMREAD_GRAYSCALE)
        # plt.imshow(im_s); plt.show()
        x, y = 88, 24
        w, h = 511, 423
        im_d = im_s[y:y+h, x:x+w]

        dname = imfile.split('/')[-1]
        if is_train:
            dest_folder = TRN_DEST / vid_file.parts[-1]
        else:
            dest_folder = TEST_DEST / vid_file.parts[-1]
            # print "dest: ", dest_folder
        if not dest_folder.exists():
            dest_folder.mkdir()
        destfile = dest_folder / dname
        cv2.imwrite(destfile.__str__(), im_d)



