# !usr/bin/env python3

if __name__ == "__main__":
    from manager.context_manager import timer
    from decorator.template import function

    def stressfull_test():
        for _ in range(99999999):
            pass
    
    print("Rodando com gerenciador de contexto")

    with timer():
        stressfull_test()
    
    @function
    def callme():
        stressfull_test()
    
    print('Rodando com gerenciador de contexto e decorator.')
    with  timer():
        callme()