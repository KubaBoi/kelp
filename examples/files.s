; File Handling System Calls
; %eax      %name       %ebx            %ecx        %edx
; 2         sys_fork    struct pt_regs  -           -
; 3         sys_read    uint            char*       size_t
; 4         sys_write   uint            const char* size_t
; 5         sys_open    const char*     int         int
; 6         sys_close   uint            -           -
; 8         sys_creat   const char*     int         -
; 19        sys_lseek   uint            off_t       uint

;CREATE
;    Put the system call sys_creat() number 8, in the EAX register.
;    Put the filename in the EBX register.
;    Put the file permissions in the ECX register.
; 
; The system call returns the file descriptor of the created file
; in the EAX register, in case of error, 
; the error code is in the EAX register.

;OPEN
;    Put the system call sys_open() number 5, in the EAX register.
;    Put the filename in the EBX register.
;    Put the file access mode in the ECX register.
;    Put the file permissions in the EDX register.
; 
; Among the file access modes, most commonly used are:
;  read-only (0), write-only (1), and read-write (2).

;READ
;    Put the system call sys_read() number 3, in the EAX register.
;    Put the file descriptor in the EBX register.
;    Put the pointer to the input buffer in the ECX register.
;    Put the buffer size, i.e., the number of bytes to read, 
;           in the EDX register.

;CLOSE
;    Put the system call sys_close() number 6, in the EAX register.
;    Put the file descriptor in the EBX register.

;UPDATE
;    Put the system call sys_lseek () number 19, in the EAX register.
;    Put the file descriptor in the EBX register.
;    Put the offset value in the ECX register.
;    Put the reference position for the offset in the EDX register.
;
; The reference position could be:
;    Beginning of file - value 0
;    Current position - value 1
;    End of file - value 2

section	.text
   global _start         ;must be declared for using gcc
	
_start:                  ;tell linker entry point
   ;create the file
   mov  eax, 8
   mov  ebx, file_name
   mov  ecx, 0777        ;read, write and execute by all
   int  0x80             ;call kernel
	
   mov [fd_out], eax
    
   ; write into the file
   mov	edx,len          ;number of bytes
   mov	ecx, msg         ;message to write
   mov	ebx, [fd_out]    ;file descriptor 
   mov	eax,4            ;system call number (sys_write)
   int	0x80             ;call kernel
	
   ; close the file
   mov eax, 6
   mov ebx, [fd_out]
    
   ; write the message indicating end of file write
   mov eax, 4
   mov ebx, 1
   mov ecx, msg_done
   mov edx, len_done
   int  0x80
    
   ;open the file for reading
   mov eax, 5
   mov ebx, file_name
   mov ecx, 0             ;for read only access
   mov edx, 0777          ;read, write and execute by all
   int  0x80
	
   mov  [fd_in], eax ; file descriptor
    
   ;read from file
   mov eax, 3
   mov ebx, [fd_in]
   mov ecx, info
   mov edx, 26
   int 0x80
    
   ; close the file
   mov eax, 6
   mov ebx, [fd_in]
   int  0x80    
	
   ; print the info 
   mov eax, 4
   mov ebx, 1
   mov ecx, info
   mov edx, 26
   int 0x80
       
   mov	eax,1             ;system call number (sys_exit)
   int	0x80              ;call kernel

section	.data
file_name db 'myfile.txt', 0 ; bacha na koncovy nuly
msg db 'Welcome to Tutorials Point', 0
len equ  $-msg

msg_done db 'Written to file', 0xa
len_done equ $-msg_done

section .bss
fd_out resb 1
fd_in  resb 1
info resb  26








