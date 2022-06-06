import ycmd
class bypass(): 
  def ply(self,gid,ocmd):
    //ループするときに使う
    def nextqueue(e):
      ncmd = ycmd.ycmd.CMD()
      ncmd.var['ocmd'] = ocmd
      ncmd.var['gid'] = gid
      loop = asyncio.get_event_loop()
      asyncio.run_coroutine_threadsafe(ncmd.cmdrun_method_file("botcmd/play.ycmd","nextqueue"),loop)
    ocmd.getvar('vcc').play(ocmd.getvar('fpa'),after=nextqueue)
