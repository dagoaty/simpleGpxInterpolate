# imports
import gpxpy
import gpxpy.gpx

# main
def main() -> None:
    gpx_file = open('route.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

    points: list[tuple[float, float]] = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append((point.latitude, point.longitude))

    new_points: list[tuple[float, float]] = []
    for pos, p in enumerate(points):
        new_points.append(p)
        if pos < len(points) - 1:
            print(p[0], points[pos+1][0])
            new_lat = round((p[0] + points[pos+1][0]) / 2, 8)
            new_lon = round((p[1] + points[pos+1][1]) / 2, 8)
            new_points.append((new_lat, new_lon))

    new_gpx: gpxpy.gpx.GPX = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    new_gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)
    for p in new_points:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(p[0], p[1]))

    with open('route_interpolated.gpx', 'w') as f:
        f.write(new_gpx.to_xml())

if __name__ == '__main__':
    main()