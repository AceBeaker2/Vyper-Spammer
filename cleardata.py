def cleardata(path):
    import os
    import shutil
    try:
        shutil.rmtree(path)
        #shutil.rmtree('fakedata')
    except:
        pass
    #os.mkdir('maildata')
    os.mkdir(path)
