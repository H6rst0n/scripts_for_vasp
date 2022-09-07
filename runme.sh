mkdir -p $HOME/scripts
cd $HOME/scripts
git clone https://github.com/H6rst0n/scripts_for_vasp.git
cd ./scripts_for_vasp
chmod +x *py *sh
echo 'export PATH=$HOME/scripts/scripts_for_vasp:$PATH' >> ~/.bashrc
echo 'module load anaconda3/5.1.10' >> ~/.bashrc
source ~/.bashrc
