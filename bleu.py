import os	
import subprocess
import re
import argparse

def moses_multi_bleu(hyp_file, ref_file, lowercase=False):
    """Calculate the bleu score for hypotheses and references
    using the MOSES ulti-bleu.perl script.
    Args:
    hypotheses: A numpy array of strings where each string is a single example.
    references: A numpy array of strings where each string is a single example.
    lowercase: If true, pass the "-lc" flag to the multi-bleu script
    Returns:
    The BLEU score as a float32 value.
    """

    # if np.size(hypotheses) == 0:
    #     return np.float32(0.0)

    
    # # Get MOSES multi-bleu script
    # try:
    #     multi_bleu_path, _ = urllib.request.urlretrieve("https://raw.githubusercontent.com/moses-smt/mosesdecoder/master/scripts/generic/multi-bleu.perl")
    #     os.chmod(multi_bleu_path, 0o755)
    # except: #pylint: disable=W0702
    #     print("Unable to fetch multi-bleu.perl script, using local.")
    #     metrics_dir = os.path.dirname(os.path.realpath(__file__))
    #     bin_dir = os.path.abspath(os.path.join(metrics_dir, "..", "..", "bin"))
    #     multi_bleu_path = os.path.join(bin_dir, "utils/multi-bleu.perl")
    multi_bleu_path = "utils/multi-bleu.perl"
    os.chmod(multi_bleu_path, 0o755)


    # Dump hypotheses and references to tempfiles
    # hypothesis_file = tempfile.NamedTemporaryFile()
    # hypothesis_file.write("\n".join(hypotheses).encode("utf-8"))
    # hypothesis_file.write(b"\n")
    # hypothesis_file.flush()
    # reference_file = tempfile.NamedTemporaryFile()
    # reference_file.write("\n".join(references).encode("utf-8"))
    # reference_file.write(b"\n")
    # reference_file.flush()


     # Calculate BLEU using multi-bleu script
    with open(hyp_file, "r") as read_pred:
        bleu_cmd = [multi_bleu_path]
        if lowercase:
            bleu_cmd += ["-lc"]
        bleu_cmd += [ref_file]
        try:
            bleu_out = subprocess.check_output(bleu_cmd, stdin=read_pred, stderr=subprocess.STDOUT)
            bleu_out = bleu_out.decode("utf-8")
            bleu_score = re.search(r"BLEU = (.+?),", bleu_out).group(1)
            bleu_score = float(bleu_score)
        except subprocess.CalledProcessError as error:
            if error.output is not None:
                print("multi-bleu.perl script returned non-zero exit code")
                print(error.output)
                bleu_score = np.float32(0.0)

    # Close temp files
    # hypothesis_file.close()
    # reference_file.close()
    return bleu_score

#pylint: disable=C0103

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="gvt-64")
    parser.add_argument("--hyp", type=str, default=None)
    parser.add_argument("--ref", type=str, default=None)
    arg = parser.parse_args()
    hyp_file = os.path.join(arg.path, arg.hyp)
    ref_file = os.path.join(arg.path, arg.ref) 
    print(moses_multi_bleu(hyp_file, ref_file))


if __name__ == '__main__':
    main()
