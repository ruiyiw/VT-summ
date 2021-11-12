PATH=save/gvt-128-pre/pre-trs-1000

grep "^Greedy:" ${PATH}/result.txt > ${PATH}/greedy.txt
sed 's/Greedy://1' ${PATH}/greedy.txt > ${PATH}/hyp.txt
grep "^Ref:" ${PATH}/result.txt > ${PATH}/example.txt
sed 's/Ref://1' ${PATH}/example.txt > ${PATH}/ref.txt
python3 score.py --path ${PATH} --hyp hyp.txt --ref ref.txt
python3 bleu.py --path ${PATH} --hyp hyp.txt --ref ref.txt
