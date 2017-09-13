var app = angular.module('myApp', []);
app.controller('formCtrl', function($scope,$http) {

    $scope.getMappings = function() {
        $http.get("http://localhost/"+$scope.fellows+"/"+$scope.videos)
    .then(function(response) {
        $scope.results = response.data;
    });

    };
});