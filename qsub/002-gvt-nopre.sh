cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

# 002-gvt-nopre
# Train on gvt-128 with 2000 epochs, no pre-train
python3 main.py --dataset gigaword --model cvaetrs --epochs 2000 --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 64 --gradient_accumulation_steps 2 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path save/gvt-128-nopre/model/ > save/gvt-128-nopre/out.txt
