

# for frontend 
# const payload = {
#   date: new Date().toISOString(), // Example: "2023-10-15T00:00:00Z"
#   start_time: "00:00:00",
#   end_time: "01:00:00",
# };

# const response = await fetch(`/api/timetable/${eventId}/`, {
#   method: "PUT",
#   headers: {
#     "Content-Type": "application/json",
#     Authorization: `Bearer ${token}`,
#   },
#   body: JSON.stringify(payload),
# });


# class TimetableUpdate(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def put(self, request, pk):
#         timetable = get_object_or_404(Timetable, id=pk, user=request.user)

#         serializer = TimetableSerializer(timetable, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# todo for now = timezone, profile-viewer then given to ratul 