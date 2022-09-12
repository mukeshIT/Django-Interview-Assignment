class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('member_firstname','member_middlename','member_lastname','member_gender',
                  'member_contact','member_photo','member_address')

class UserSerializer(serializers.ModelSerializer):
    reg_data = MemberSerializer()

    class Meta:
        model = User
        fields = ('username','password','reg_data',)

        def create(self, validated_data):
            reg_info = validated_data.pop('reg_data')
            user_reg = User.objects.create(**validated_data)

            user_reg.set_password(validated_data['password'])
            user_reg.save()

            Member.objects.create(user=user_reg, **reg_info)
            obj = User.objects.get(id=user_reg.id)
            return obj

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book_name','book_author','book_isbn')

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ('librarian_firstname','librarian_middlename','librarian_lastname',
                  'librarian_gender','librarian_contact','librarian_photo','librarian_address')

class LibrarianUserSerializer(serializers.ModelSerializer):
    reg_data_l = LibrarianSerializer()

    class Meta:
        model = User
        fields = ('username','password','reg_data_l',)

        def create(self, validated_data):
            reg_info = validated_data.pop('reg_data_l')
            user_reg = User.objects.create(**validated_data)

            user_reg.set_password(validated_data['password'])
            user_reg.save()

            Librarian.objects.create(user=user_reg, **reg_info)
            obj = User.objects.get(id=user_reg.id)
            return obj