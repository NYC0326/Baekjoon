#include <stdio.h>
#include <stdlib.h>

typedef int element;	// 요소의 타입
typedef struct QueueNode {	// 큐의 노드의 타입 
	element data;
	struct QueueNode *link;
} QueueNode;

typedef struct {		// 큐 ADT 구현
	QueueNode *front, *rear;
} LinkedQueueType;

// 큐 초기화 함수
void init(LinkedQueueType *q){
	// 구현
}

// 공백 상태 검출 함수
int is_empty(LinkedQueueType *q){
	// 구현
}

// 포화 상태 검출 함수
int is_full(LinkedQueueType *q){
	return 0;
}

// 삽입 함수
void enqueue(LinkedQueueType *q, element data){
	// 구현
}

// 삭제 함수
element dequeue(LinkedQueueType *q){
	QueueNode *temp =q-> front;
	element data;
	if (is_empty(q)) {		// 공백상태
		fprintf(stderr, "스택이 비어있음\n");
		exit(1);
	}
	else {
		// 구현
	}
}

void print_queue(LinkedQueueType *q){
	QueueNode *p;
	for (p= q->front; p != NULL; p = p->link)
		printf("%d->", p->data);
	printf("NULL\n");
}

// 연결된 큐 테스트 함수
int main(void)
{
	LinkedQueueType queue;

	init(&queue);		// 큐 초기화

	enqueue(&queue, 1);	print_queue(&queue);
	enqueue(&queue, 2);	print_queue(&queue);
	enqueue(&queue, 3);	print_queue(&queue);
	dequeue(&queue);		print_queue(&queue);
	dequeue(&queue);		print_queue(&queue);
	dequeue(&queue);		print_queue(&queue);
	return 0;
}
