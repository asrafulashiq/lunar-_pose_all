#!/bin/bash
# cd data
VID_FLDR='./videos'
DEST_FLDR='./raw_images'
for vid_file in `ls ${VID_FLDR}`; do
    echo "$vid_file"
    IFS="." read -ra ADDR <<< "${vid_file}"
    main_name=${ADDR[0]}
    dest=${DEST_FLDR}/${main_name}
    mkdir $dest
    ffmpeg -i ${VID_FLDR}/${vid_file} ${dest}/frame%05d.jpg -hide_banner
done
