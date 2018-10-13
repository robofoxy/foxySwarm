echo "Running....."
roscore >/dev/null 2>&1 &
rosrun master_discovery_fkie master_discovery >/dev/null 2>&1 &
rosrun master_sync_fkie master_sync >/dev/null 2>&1 &
sleep 5
echo ""
echo "Available ROS topics:"
rostopic list
echo ""
echo "Environmet variables are ready."
echo "If not, run:"
echo " killall -9 roscore"
echo " killall -9 master_discovery"
echo " killall -9 master_sync"
echo "OR"
echo "./exit.sh"
echo ""
