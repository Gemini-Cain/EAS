import stat
import pexpect


    child = pexpect.spawn("scp 1.cpp bppf_eas@192.168.87.3:/u1/bppf_eas")   //拷贝到本地目录
    child.expect("bppf_eas@192.168.87.3's password:")
    child.sendline("123456")
    child.interact()
    os.chmod(sqldb,stat.S_IRWXU)   //把复制到本地的database改为可读写格式