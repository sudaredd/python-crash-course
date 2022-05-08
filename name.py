#python
# -*- coding: utf-8 -*-
#
#  name.py
#  
#  Copyright 2022 sudar <sudar@DESKTOP-VMET04L>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    name = "ada lovelace"
    print(name.title())
    name = "Ada Lovelace"
    print(name.upper())
    print(name.lower())
    
    first_name = "Ada"
    last_name = "Lovelace"
    full_name = first_name + " "+ last_name;
    print(full_name)
    print("Hello," + full_name + "!")
    print("Languages:\n\tPython\n\tC\n\tJavaScript")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
