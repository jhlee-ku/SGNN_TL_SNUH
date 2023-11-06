def convert(savepath=None,filename=None,data=None,allow_nan=True):
    import numpy as np
    if savepath == None:
        print("Please put save path!!!")
        raise
    if filename == None:
        filename = "converted_mplus_input"
        print("Filename has not been given. Default naming (converted_mplus_input) will used")
    if np.all(data) == None:
        print("Please put data!!!")
        raise
    data = data.values.tolist()
    with open(savepath+"/"+filename+".dat", "w") as file:
        for idx in range(len(data)):
#             assert len(data[idx])==60
            for idx2 in range(len(data[idx])):
                if data[idx][idx2] != 0.0 and data[idx][idx2] != 1.0 and data[idx][idx2] != 2.0:
                    if allow_nan ==False:
                        file.write("%.6f" % 0)
                    if allow_nan ==True:
                        file.write('*')
                    file.write('\t')
                else:
                    file.write("%.6f" % data[idx][idx2])
                    file.write('\t')
            file.write("\n")
        file.close()
        
    return

def get_fs_score(datapath=None,num_factors=None):
    import numpy as np
    import pandas as pd
    if datapath == None or num_factors ==None or type(num_factors) !=int:
        print("Please put data path & number of factors!!!")
        raise
    result = pd.read_csv(datapath,header=None)
    result_df = pd.DataFrame(index=result.index,columns=np.arange(1,num_factors+1,1))
    for fac in range(num_factors):
        reverse_num = num_factors-fac
        fs_list = []
        for val in result.values:
            fs = str(val).split('    ')[-2*reverse_num]
            fs_list.append(fs)
        fs_float = np.array(fs_list).astype(float)
        assert len(fs_float) == len(result)
        result_df[fac+1] = fs_float
    return result_df
