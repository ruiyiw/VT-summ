from rouge import FilesRouge
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="gvt-64")
    parser.add_argument("--hyp", type=str, default=None)
    parser.add_argument("--ref", type=str, default=None)
    arg = parser.parse_args()
    hyp_file = os.path.join(arg.path, arg.hyp)
    ref_file = os.path.join(arg.path, arg.ref)
    files_rouge = FilesRouge()
    scores = files_rouge.get_scores(hyp_file, ref_file)
    rouge_1 = [score['rouge-1']['f'] for score in scores]
    rouge_2 = [score['rouge-2']['f'] for score in scores]
    rouge_l = [score['rouge-l']['f'] for score in scores]
    print("rouge-1 = {}".format(sum(rouge_1) / len(rouge_1)))
    print("rouge-2 = {}".format(sum(rouge_2) / len(rouge_2)))
    print("rouge-l = {}".format(sum(rouge_l) / len(rouge_l)))
    

if __name__ == "__main__":
    main()
