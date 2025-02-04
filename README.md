# nvidia-gpu-fan-control
Script ontrolling PWM Fans based on the temp of a NVidia GPU (in my case, a m40)

Edits are made to the file "/sys/class/hwmon/hwmon1/pwm3" file in my case to set a fan speed between 0 and 255. Use "sudo pwmconfig" to determine the file you need to edit based on which pwm fan you are working with.

If the temp is over 45*C, fan speed is set to max (255), otherwise set to 100.

What this translates to in my use case is when I am actively using Ollama and the gpu temps rise while doing work, the fans run. When things are idle, they slow down. I need to use this since the m40 gpu is passively cooled. In my case, it is mounted in a crypto mining rig frame with external fans.


