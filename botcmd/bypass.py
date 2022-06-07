import ycmd
import asyncio
async def cmf(file,fuc,ccc):
  await ccc.cmdrun_method_file(file,fuc)
class bypass(): 
  async def ply(self,gid,ocmd):
    loop = asyncio.get_event_loop()
    def nextqueue(e):
      ncmd = ycmd.ycmd.CMD()
      ncmd.var['ocmd'] = ycmd.ClassData.ClassData(ocmd)
      ncmd.var['gid'] = ycmd.ClassData.ClassData(gid)
      asyncio.run_coroutine_threadsafe(cmf("botcmd/play.ycmd","nextqueue",ncmd),loop)
    ocmd.getvar('vcc').play(ocmd.getvar('fpa'),after=nextqueue)
