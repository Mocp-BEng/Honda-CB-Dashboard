def drawArcFloat(self, center: Vector, width: float, height: float, angle: Radians,
                 draw_angles: Optional[Tuple[Radians, Radians]], properties: Properties):
        if min(width, height) < 1e-5:
            return  # matplotlib crashes if the arc has almost 0 size

        if draw_angles is None:
            start_degrees, end_degrees = 0, 360
        else:
            # draw angles are relative to `angle`. The arc is drawn anticlockwise from start to end.
            # draw_angles are *NOT* in the global coordinate system, but instead are angles inside the
            # local coordinate system defined by the major and minor axes of the ellipse
            # (where the ellipse looks like a circle)
            ratio = height / width
            start, end = param_to_angle(ratio, draw_angles[0]), param_to_angle(ratio, draw_angles[1])
            start_degrees, end_degrees = degrees(start), degrees(end)

        arc = Arc((center.x, center.y), width, height, color=properties.color, linewidth=self.line_width,
                  angle=degrees(angle), theta1=start_degrees, theta2=end_degrees, zorder=self._get_z())
        self.ax.add_patch(arc) 