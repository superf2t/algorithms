#!/usr/bin/env python
#-*- coding:utf-8 -*-

def sorter(func):
	def wrapper(elements,**kwargs):
		print 'before sort:%s'%elements
		print 'call sort function %s()'%func.__name__
		func(elements,**kwargs)
		print 'after sort:%s'%elements
	return wrapper

@sorter
def insert_sort(elements):
	for i in range(len(elements)):
		temp=elements[i]
		j=i
		while j>0 and elements[j-1]>temp:
			elements[j]=elements[j-1]
			j-=1
		elements[j]=temp

@sorter
def bubble_sort(elements):
	for i in range(len(elements)-1):
		j=0
		while j<len(elements)-1-i:
			if elements[j]>elements[j+1]:
				temp=elements[j+1]
				elements[j+1]=elements[j]
				elements[j]=temp
			j+=1

@sorter
def shell_sort(elements):
	d=len(elements)/2
	while d>0:
		for i in range(d,len(elements)):
			temp = elements[i]
			j = i
			while j>=d and elements[j-d]>temp:
				elements[j]=elements[j-d]
				j-=d
			elements[j]=temp
		d/=2

@sorter
def quick_sort(elements):
	def quick_sub_sort(elements,low,high):
		if low<high:
			i,j=low,high
			pivot = elements[low]
			while i<j:
				while j>i:
					if elements[j]<pivot:
						elements[i]=elements[j]
						break
					j-=1
				while i<j:
					if elements[i]>pivot:
						elements[j]=elements[i]
						break
					i+=1
			elements[i]=pivot
			quick_sub_sort(elements,low,i-1)
			quick_sub_sort(elements,i+1,high)

	quick_sub_sort(elements,0,len(elements)-1)

@sorter
def merge_sort(elements):
	def merge(elements,low,mid,high):
		i,j,k=low,mid+1,0
		temp=[0 for x in range(low,high+1)]
		while i<=mid and j<=high:
			if elements[i]>elements[j]:
				temp[k]=elements[j]
				k+=1
				j+=1
			else:
				temp[k]=elements[i]
				k+=1
				i+=1
		while i<=mid:
			temp[k]=elements[i]
			k+=1
			i+=1
		while j<high:
			temp[k]=elements[j]
			k+=1
			j+=1
		i,k=low,0
		while i<=high:
			elements[i]=temp[k]
			k+=1
			i+=1

	def merge_sub_sort(elements,low,high):
		if low < high:
			mid = (low+high)/2
			merge_sub_sort(elements,low,mid)
			merge_sub_sort(elements,mid+1,high)
			merge(elements,low,mid,high)

	merge_sub_sort(elements,0,len(elements)-1)

@sorter
def heap_sort(elements):
	def heap_adjust(elements,n,i):
		while i<n:
			j=2*i+1

			if j+1>n and j>n:
				break

			if j+1<=n:
				if elements[j]<elements[j+1]:
					j=j+1

			if elements[i]<elements[j]:
				temp=elements[j]
				elements[j]=elements[i]
				elements[i]=temp
				i=j
			else: break

	def build_heap(elements):
		i=(len(elements)-1)/2
		while i>=0:
			heap_adjust(elements,len(elements)-1,i)
			i-=1

	build_heap(elements)
	i=len(elements)-1
	while i>0:
		temp = elements[0]
		elements[0]=elements[i]
		elements[i]=temp

		heap_adjust(elements,i-1,0)
		i-=1


if __name__=='__main__':
	test = [7,5,2,1,4,6,3]
	# insert_sort(test)
	# bubble_sort(test)
	# shell_sort(test)
	# quick_sort(test)
	# merge_sort(test)
	heap_sort(test)
