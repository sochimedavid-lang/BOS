import subprocess,sys
CUT={'01':6.90,'02':6.47,'03':6.20,'04':12.30,'05':5.70,'06':6.17,'07':None,'08':14.00,'09':7.94,'10':5.97}
CARD=2.5; XF=0.25
for k,c in CUT.items():
    src=f'batana_hommes/batana_{k}.mp4'
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    if c is None: c=d-0.05
    T=c+CARD-XF
    fc=(f"[0:v]trim=0:{c},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p[v0];"
        f"[1:v]format=rgba,fade=in:st=0:d=0.15:alpha=1,fade=out:st=2.35:d=0.2:alpha=1[h];"
        f"[v0][h]overlay=0:0:eof_action=pass,format=yuv420p[vh];"
        f"[2:v]zoompan=z='min(1+0.0010*in,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p,setsar=1[cd];"
        f"[vh]setsar=1[vh2];[vh2][cd]xfade=transition=fade:duration={XF}:offset={c-XF:.3f}[v];"
        f"[3:a]atrim=0:{T:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={T-0.8:.3f}:d=0.8[a]")
    cmd=['ffmpeg','-v','error','-y','-i',src,'-loop','1','-framerate','30','-t','2.6','-i',f'prod/hook_{k}.png',
         '-loop','1','-framerate','30','-t',str(CARD),'-i','prod/card.png','-stream_loop','-1','-i',src,
         '-filter_complex',fc,'-map','[v]','-map','[a]','-t',f'{T:.3f}','-c:v','libx264','-preset','medium','-crf','19','-r','30',
         '-c:a','aac','-b:a','192k','-movflags','+faststart',f'prod/peryal_batana_{k}.mp4']
    r=subprocess.run(cmd,capture_output=True,text=True)
    print(k, 'OK' if r.returncode==0 else r.stderr[-600:], f'{T:.1f}s')
