import sys
import re

def _get_port_info(pattern):

    out="switchName:\tFabricA-Server\nswitchType:\t109.1\nswitchState:\tOnline   \nswitchMode:\tNative\nswitchRole:\tPrincipal\nswitchDomain:\t2\nswitchId:\tfffc02\nswitchWwn:\t10:00:00:27:f8:6f:13:56\nzoning:\t\tON (PureArray1)\nswitchBeacon:\tOFF\nFC Router:\tOFF\nHIF Mode:\tOFF\nAllow XISL Use:\tOFF\nLS Attributes:\t[FID: 128, Base Switch: No, Default Switch: Yes, Ficon Switch: No, Address Mode 0]\n\nIndex Port Address  Media Speed   State       Proto\n==================================================\n   0   0   020000   --    10G\t  No_Module   FC  LS \n   1   1   020100   --    8G \t  No_Module   FC  \n   2   2   020200   --    8G \t  No_Module   FC  \n   3   3   020300   --    8G \t  No_Module   FC  \n   4   4   020400   --    8G \t  No_Module   FC  \n   5   5   020500   --    8G \t  No_Module   FC  \n   6   6   020600   --    8G \t  No_Module   FC  \n   7   7   020700   --    8G \t  No_Module   FC  \n   8   8   020800   id    16G\t  Online      FC  F-Port  10:00:8c:7c:ff:29:e8:00 \n   9   9   020900   id    16G\t  Online      FC  F-Port  21:00:00:24:ff:19:bb:42 \n  10  10   020a00   --    8G \t  No_Module   FC  \n  11  11   020b00   --    8G \t  No_Module   FC  \n  12  12   020c00   id    N16\t  No_Light    FC  \n  13  13   020d00   id    8G \t  No_Light    FC  \n  14  14   020e00   --    8G \t  No_Module   FC  \n  15  15   020f00   --    8G \t  No_Module   FC  \n  16  16   021000   --    N16\t  No_Module   FC  \n  17  17   021100   --    N16\t  No_Module   FC  \n  18  18   021200   --    N16\t  No_Module   FC  \n  19  19   021300   --    N16\t  No_Module   FC  \n  20  20   021400   --    N16\t  No_Module   FC  \n  21  21   021500   --    N16\t  No_Module   FC  \n  22  22   021600   --    N16\t  No_Module   FC  \n  23  23   021700   --    N16\t  No_Module   FC  \n  24  24   021800   --    N16\t  No_Module   FC  \n  25  25   021900   --    N16\t  No_Module   FC  \n  26  26   021a00   --    N16\t  No_Module   FC  \n  27  27   021b00   --    N16\t  No_Module   FC  \n  28  28   021c00   --    N16\t  No_Module   FC  \n  29  29   021d00   --    N16\t  No_Module   FC  \n  30  30   021e00   --    16G\t  Online      FC  SIM-Port 20:1e:00:27:f8:6f:13:56 \n  31  31   021f00   --    16G\t  Online      FC  SIM-Port 20:1f:00:27:f8:6f:13:56 \n  32  32   022000   --    16G\t  Online      FC  SIM-Port 20:20:00:27:f8:6f:13:56 \n  33  33   022100   --    16G\t  Online      FC  SIM-Port 20:21:00:27:f8:6f:13:56 \n  34  34   022200   --    16G\t  Online      FC  SIM-Port 20:22:00:27:f8:6f:13:56 \n  35  35   022300   --    16G\t  Online      FC  SIM-Port 20:23:00:27:f8:6f:13:56 \n  36  36   022400   --    16G\t  Online      FC  SIM-Port 20:24:00:27:f8:6f:13:56 \n  37  37   022500   --    16G\t  Online      FC  SIM-Port 20:25:00:27:f8:6f:13:56 \n  38  38   022600   --    16G\t  Online      FC  SIM-Port 20:26:00:27:f8:6f:13:56 \n  39  39   022700   --    16G\t  Online      FC  SIM-Port 20:27:00:27:f8:6f:13:56 \n"
    lines = out.split('\n')
    matches = []
#    reg_str = "r'" + " +" + pattern + " +" + pattern + "'"
    reg_str = " +" + pattern + " +" + pattern
    print(reg_str)
    reg = re.compile(reg_str)
    for line in lines:
        print(line)
        matches = re.search(reg, line)
        if (matches):
            return line


s=sys.argv[1]
l=_get_port_info(s)
print(l)


