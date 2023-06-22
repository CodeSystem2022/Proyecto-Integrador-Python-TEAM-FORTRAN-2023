import logging as log   


# Configurar el nivel de registro y el formato de los mensajes de registro

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',# Formato del mensaje de registro
                datefmt='%I:%M:%S %p',# Formato de la fecha y hora del mensaje de registro
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('DEBUG')
    log.debug('INFO')
    log.warning('WARNING')
    log.error('ERROR')
    log.critical('CRITICAL')


