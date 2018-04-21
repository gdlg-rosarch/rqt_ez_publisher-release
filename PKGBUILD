# Script generated with Bloom
pkgdesc="ROS - The rqt_ez_publisher package"
url='http://wiki.ros.org/rqt_ez_publisher'

pkgname='ros-lunar-rqt-ez-publisher'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-catkin_pkg'
'ros-lunar-catkin'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
)

depends=('ros-lunar-geometry-msgs'
'ros-lunar-rospy'
'ros-lunar-rqt-gui'
'ros-lunar-rqt-gui-py'
'ros-lunar-rqt-py-common'
'ros-lunar-tf'
'ros-lunar-tf2-msgs'
)

conflicts=()
replaces=()

_dir=rqt_ez_publisher
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_ez_publisher $srcdir/rqt_ez_publisher
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

