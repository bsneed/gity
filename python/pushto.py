# Copyright Aaron Smith 2009
# 
# This file is part of Gity.
# 
# Gity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Gity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Gity. If not, see <http://www.gnu.org/licenses/>.
from _util import *
try:
	import re,os,subprocess,simplejson as json
except Exception,e:
	sys.stderr.write(str(e))
	exit(84)
command=""
try:
	from _argv import *
	if not options.misc: raise Exception("Gitty Error: The push to command requires a remote and a branch.")
	remote=sanitize_str(options.misc[0])
	branch=sanitize_str(options.misc[1])
	command="%s %s %s refs/heads/%s:refs/heads/%s" % (options.git,"push",remote,branch,branch)
	rcode,stout,sterr=run_command(command)
	if cant_push_to_newer_remote(sterr): exit(91)
	if cant_push_to(sterr): exit(90)
	if server_hung_up(sterr): exit(85)
	if server_unreachable(sterr): exit(86)
	rcode_for_git_exit(rcode,sterr)
	exit(0)
except Exception, e:
	sys.stderr.write("The push to command through this error: " + str(e))
	sys.stderr.write("\ncommand: %s" % command)
	log_gity_version(options.gityversion)
	log_gitv(options.git)
	exit(84)