Name:           ros-lunar-rqt-ez-publisher
Version:        0.4.0
Release:        0%{?dist}
Summary:        ROS rqt_ez_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_ez_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-rospy
Requires:       ros-lunar-rqt-gui
Requires:       ros-lunar-rqt-gui-py
Requires:       ros-lunar-rqt-py-common
Requires:       ros-lunar-tf
Requires:       ros-lunar-tf2-msgs
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-sensor-msgs

%description
The rqt_ez_publisher package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat May 06 2017 Takashi Ogura <t.ogura@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

