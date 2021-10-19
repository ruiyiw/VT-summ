cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 64 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path_pretrained trs-64/trs/model_epoch299_iter277770_2.9944_19.9735_0.0000_12.2900_0.0000 --save_path gvt-64-pre/cvae_trs_e299/ > gvt-64-pre/cvae_trs_e299/out.txt
