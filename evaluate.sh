grep "^Greedy:" gvt-64-pre/cvae_trs_e299/out_e1000.txt > greedy.txt
sed 's/Greedy://1' greedy.txt > hyp_e1000.txt
mv hyp_e1000.txt gvt-64-pre/cvae_trs_e299/
grep "^Ref:" gvt-64-pre/cvae_trs_e299/out_e1000.txt > example.txt
sed 's/Ref://1' example.txt > ref_e1000.txt
mv ref_e1000.txt gvt-64-pre/cvae_trs_e299/
python3 score.py --path gvt-64-pre/cvae_trs_e299 --hyp hyp_e1000.txt --ref ref_e1000.txt
python3 bleu.py --path gvt-64-pre/cvae_trs_e299 --hyp hyp_e1000.txt --ref ref_e1000.txt
