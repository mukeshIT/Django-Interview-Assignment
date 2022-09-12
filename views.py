class LibrarianAPI(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    # authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated ,)
    serializer_class = UserSerializer

class MemberAPI(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    # authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated ,)
    serializer_class = UserSerializer

class BooksAPI(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    # authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated ,)
    serializer_class = BookSerializer