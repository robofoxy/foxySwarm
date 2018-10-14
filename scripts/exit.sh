echo "Killing roscore and scripts..."
sudo killall -9 roscore
killall -9 master_discovery
killall -9 master_sync
echo ""
echo "DONE"
