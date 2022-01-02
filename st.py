import speedtest
import math
import time

helper = speedtest.Speedtest()

helper.get_best_server()
helper.download()
helper.upload()

result = helper.results.dict()

download = result.get('download')
upload = result.get('upload')



mbDownload = download / 1e+6
mbUpload = upload / 1e+6

timeStr = time.strftime('%c', time.localtime(time.time()))


print(f'[{timeStr}] 다운로드: {mbDownload}Mbps 업로드: {mbUpload}Mbps')

