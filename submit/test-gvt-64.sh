cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --test --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 128 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path_pretrained gvt-64/cvae_new_bow_batch/model_15999_14.6016_61.0199_0.0000_0.6100_10.4904 > gvt-64/test_out.txt 
