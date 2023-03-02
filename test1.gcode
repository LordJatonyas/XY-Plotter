; Plotter Test 1:
; A box within a box within a box

G90                 ; absolute mode
F1000               ; set draw speed
M8                  ; pen up
G0 X40 Y40          ; move to box 1 start location
M9                  ; pen down
G1 X40 Y160         ; box 1
G1 X160 Y160        ; box 1
G1 X160 Y40         ; box 1
G1 X40 Y40          ; box 1
M8                  ; pen up
G0 X65 Y65          ; move to box 2 start location
M9                  ; pen down
G1 X135 Y65         ; box 2
G1 X135 Y135        ; box 2
G1 X65 Y135         ; box 2
G1 X65 Y65          ; box 2
M8                  ; pen up
G0 X90 Y90          ; move to box 3 start location
M9                  ; pen down
G1 X90 Y110         ; box 3
G1 X110 Y110        ; box 3
G1 X110 Y90         ; box 3
G1 X90 Y90          ; box 3
M8                  ; pen up
G0 X0 Y0            ; feed paper out
;M8                  ; pen down (lower power)
M2                  ; end
