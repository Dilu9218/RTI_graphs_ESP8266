%#!/usr/bin/octave -qf

pkg load communications
pkg load statistics

% dimentions of the terrain
width=20;
height=20;

% N is the number of voxels in the image
N = width * height;

% W is the weight matrix which will get populated on the go
W=[];

% coordinates of the wireless nodes
coords=[5,1;
    10,1;
    15,1;
    1,10;
    5,20;
    10,20;
    15,20;
    20,10;];

% number of nodes
num_nodes=length(coords)

% number of links (this will get updated shortly)
num_links=0;

% link matrix (this will get updated shortly)
links=[];

%to store pixels
linkPixel=[];

X = zeros(width, height);

%initialize count
count=1;

% generating weight matrix
for i=1:length(coords)
	for j=i+1:length(coords)
		num_links=num_links+1;
    		disp(num_links);
		% start and end point of line
		a=[coords(i,1), coords(i,2)];
		b=[coords(j,1), coords(j,2)];
    %disp(coords(i,1));
    %disp(coords(i,2));
		%draw links between Tx to Rx
		if (or(((coords(i,1)== 1) && (coords (i,2)== 10)) , ((coords(i,1)== 20 && coords (i,2)== 10)),
    ((coords(j,1)== 1) && (coords (j,2)== 10)),((coords(j,1)== 20 && coords (j,2)== 10))))
    %eliminate two transmitters link
    if((coords(i,1)== 1) && (coords (i,2)== 10)&& (coords(j,1)== 20) && (coords (j,2)== 10))
    continue
    endif
		ab=[coords(i,1), coords(j,1);coords(i,2),coords(j,2)];
		% add the link to the links matrix for future use
		links=[links;a,b];
		%calculate euclidean link distance
		dlink=sqrt((coords(i,1)-coords(j,1))^2 +(coords(i,2)-coords(j,2))^2);
		%reinitialize the pixel store vector to store weights for each links
		%linkPixel=[];
		%k and l represents all voxels
		for k=1:width
			for l=1:height
			currentPixel= [k,l];
			%check if inside ellipse, given two link nodes as foci 
			%calculate distance from current pixel to the two node locations. if less than d+lamda, weight is 1.then normalize
			points=[coords(i,1), coords(i,2);k,l];
			points2=[coords(j,1), coords(j,2);k,l];
			d1 = pdist(points,'euclidean');
			d2 = pdist(points2,'euclidean');
			%dlink=pdist(ab,'euclidean');
      			fflush(stdout);
			dsum=d1+d2;
			%initialize lamda, width of the ellipse
			lamda=dlink/100;
			if (dsum<(dlink+lamda))
				weight= 1/sqrt(dlink);
				linkPixel=[linkPixel;k,l];
				%disp(linkPixel);
				%draw image dinamically for each link
        			X(sub2ind(size(X), linkPixel(count, 1), linkPixel(count, 2))) = weight;
				count++;
				%disp("X is");
				%X'
			%else
				%disp("weight 0");
			endif
			end
		end
		%to store linkPixel with 1
		%X = zeros(width, height);
      		if isempty(linkPixel)
	    		disp("empty");
      		else
			[mat,padded] = vec2mat(X,width);
			image(mat,'CDataMapping','scaled');
			caxis([0, 1])
			colorbar
			title('Radio Tomographic Imaging');
			pause(1)
          	endif
		%disp(X');
		W=[W;reshape(X', width*height, 1)'];
    image(W);
		endif
	end
end
disp("weights");

%check if zero determinant, for singularity
disp(det(W'*W));
disp(W'*W);

%Maximum likelihood solution should be, X=(inv(W'*W))*W'*y
%but this gives the ill posed inverse problem. Singularity problem is displayed here.
disp(inv(W'*W));

%proposed equation with covariance matrix- MAP estimator
%disp(inv(W'*W + inv(Cx)*sigma_2_N) *W'*y);


#{
% dynamically drawing the image based on different Y vectors
for i=1:10
	% generating a Y vector with sample RSSI change values
	%Y=zeros(1, num_links);
  Y=zeros(1, 12);
	%disp(Y);
	%Y(1:3)=1
	Y(randi([7 10]):randi([10 12]))=1;
	
	% generating image matrix based on Y vector 
	X=Y*W;
	disp("matrix X");
	disp(X);
	[mat,padded] = vec2mat(X,width);
	%mat

	image(mat,'CDataMapping','scaled');
	%image(mat)
	colorbar
	title('Radio Tomographic Imaging');

	pause(1)
end

#}
