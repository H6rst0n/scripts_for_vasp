mkdir -p $HOME/scripts
cd ../
mv ./scripts_for_vasp $HOME/scripts
cd $HOME/scripts/scripts_for_vasp
chmod +x *py *sh
chmod -x runme.sh
echo 'export PATH=$HOME/scripts/scripts_for_vasp:$PATH' >> ~/.bashrc
echo 'module load anaconda3/5.1.10' >> ~/.bashrc
source ~/.bashrc
