## Requirements:  
- Get detections from a detection framework 
- Save detections in pictures and videos  
- Send notification to different messengers or email
- Control sessions via messenger
- Updating the system
- Scheduling the detection turn/off
- Automatic turning on/off by devices (e.g. when user's phone is in local net then detection is getting off)
- UI
- Configurable
- Face Detection for turning off

## Terms:
- detections framework(DF) - detecting motions program (like [Motion project](https://motion-project.github.io))
- agent - for local running control
- detection - event received from the detection framework
- notification - item with the info about detection(e.g. pictures, timestamp, etc)
- client - application receiving notifications(e.g. Telegram bot)
- media - resources of detection. e.g. video/pics/sound
- session - system running
            session on - when the system runs and can get detections
            session off - when the system runs and can't get detections


