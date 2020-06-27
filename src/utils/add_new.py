from os import system

import getFaces

if __name__ == '__main__':
    path = '/lib/Auth/Facerec/roots/'
    system(f"sudo chattr -R -i {path}")
    system(f"sudo chmod -R ugo+rw {path}")
    for i in range(10):
        
        try:
            getFaces.getFaces(training=True, model_n=i)
        except:
            system(f"sudo chmod -R ugo-w {path}")
            system(f"sudo chattr -R +i {path}")
            print("\nProcess ended before Completion due to an error!")
            print(f"{i} out of 10 models trained succesfully.")
            break
    
    system(f"sudo chmod -R ugo-w {path}")
    system(f"sudo chattr -R +i {path}")
    print(f"\n10 out of 10 models trained succesfully.")
