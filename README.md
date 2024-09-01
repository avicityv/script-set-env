# script-set-env
<br>Setting environment on ubuntu ( vim, python, docker, k3s, ansible )
<br><h1>After installing, script will reboot your system, dont forget about that.</h1>
<br><b>Handwork:</b>
<br>
<ul>
  <li> ssh-keygen -t ed25519</li>
  <li>sudo usermod -aG sudo $USER</li>
  <li>git clone https://github.com/avicityv/script-set-env</li>
  <li>sudo chmod -R 777 ./script-set-env</li>
</ul>
<br>
<h2># Check installation
  <ul>
    <li>python3.9 --version</li>
    <li>ansible --version</li>
    <li>docker run hello-world</li>
    <li>sudo k3s kubectl get nodes</li>
  </ul>
  </h2>



